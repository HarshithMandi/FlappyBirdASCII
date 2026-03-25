from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import BadRequestError, ForbiddenError, NotFoundError
from app.models.application import Application, ApplicationStatus
from app.models.user import UserRole
from app.repositories.application_repository import ApplicationRepository
from app.repositories.job_repository import JobRepository
from app.repositories.user_repository import UserRepository
from app.schemas.application_schema import ApplicationCreate, ApplicationStatusUpdate


class ApplicationService:
    def __init__(
        self,
        repository: ApplicationRepository,
        user_repo: UserRepository,
        job_repo: JobRepository,
    ):
        self.repository = repository
        self.user_repo = user_repo
        self.job_repo = job_repo

    def apply(self, db: Session, payload: ApplicationCreate, actor_id: int) -> Application:
        actor = self.user_repo.get(db, actor_id)
        if not actor:
            raise NotFoundError("Actor user not found")
        if actor.role not in {UserRole.admin, UserRole.candidate}:
            raise ForbiddenError("Only candidates or admins can apply")
        if actor.role == UserRole.candidate and payload.user_id != actor.id:
            raise ForbiddenError("Candidates can only apply for themselves")

        user = self.user_repo.get(db, payload.user_id)
        if not user:
            raise NotFoundError("User not found")
        if user.role != UserRole.candidate:
            raise ForbiddenError("Only candidate users can apply")

        job = self.job_repo.get(db, payload.job_id)
        if not job:
            raise NotFoundError("Job not found")

        if self.repository.get_by_user_and_job(db, payload.user_id, payload.job_id):
            raise BadRequestError("Duplicate application is not allowed")

        application = Application(user_id=payload.user_id, job_id=payload.job_id, status=ApplicationStatus.applied)
        with db.begin():
            return self.repository.create(db, application)

    def get_application(self, db: Session, application_id: int) -> Application:
        application = self.repository.get(db, application_id)
        if not application:
            raise NotFoundError("Application not found")
        return application

    def list_applications(self, db: Session, skip: int, limit: int) -> list[Application]:
        return self.repository.list(db, skip, limit)

    def list_user_applications(self, db: Session, user_id: int, skip: int, limit: int, actor_id: int) -> list[Application]:
        actor = self.user_repo.get(db, actor_id)
        if not actor:
            raise NotFoundError("Actor user not found")
        if actor.role != UserRole.admin and actor.id != user_id:
            raise ForbiddenError("Not allowed to view other users' applications")
        user = self.user_repo.get(db, user_id)
        if not user:
            raise NotFoundError("User not found")
        return self.repository.list_by_user(db, user_id, skip, limit)

    def update_status(self, db: Session, application_id: int, payload: ApplicationStatusUpdate) -> Application:
        actor = self.user_repo.get(db, payload.processed_by)
        if not actor:
            raise NotFoundError("Actor user not found")
        if actor.role not in {UserRole.admin, UserRole.recruiter}:
            raise ForbiddenError("Only recruiters or admins can update application status")

        application = self.get_application(db, application_id)
        current = application.status
        next_status = payload.status

        if current == next_status:
            return application

        allowed = {
            ApplicationStatus.applied: {ApplicationStatus.shortlisted, ApplicationStatus.rejected},
            ApplicationStatus.shortlisted: {ApplicationStatus.rejected},
            ApplicationStatus.rejected: set(),
        }
        if next_status not in allowed.get(current, set()):
            raise BadRequestError("Unsupported status transition")

        application.status = next_status
        with db.begin():
            return self.repository.update(db, application)
