from sqlalchemy.orm import Session

from app.models.application import Application


class ApplicationRepository:
    def create(self, db: Session, application: Application) -> Application:
        db.add(application)
        db.flush()
        return application

    def get(self, db: Session, application_id: int) -> Application | None:
        return db.query(Application).filter(Application.id == application_id).first()

    def get_by_user_and_job(self, db: Session, user_id: int, job_id: int) -> Application | None:
        return db.query(Application).filter(Application.user_id == user_id, Application.job_id == job_id).first()

    def list(self, db: Session, skip: int, limit: int) -> list[Application]:
        return db.query(Application).offset(skip).limit(limit).all()

    def list_by_user(self, db: Session, user_id: int, skip: int, limit: int) -> list[Application]:
        return (
            db.query(Application)
            .filter(Application.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update(self, db: Session, application: Application) -> Application:
        db.add(application)
        db.flush()
        return application
