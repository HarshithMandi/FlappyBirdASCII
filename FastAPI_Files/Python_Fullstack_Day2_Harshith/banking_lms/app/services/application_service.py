import logging

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import BadRequestError, ForbiddenError, NotFoundError
from app.models.loan_application import LoanApplication, LoanStatus
from app.models.repayment import Repayment
from app.models.user import UserRole
from app.repositories.application_repository import ApplicationRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.repayment_repository import RepaymentRepository
from app.repositories.user_repository import UserRepository
from app.schemas.application_schema import LoanApplicationCreate, LoanApplicationStatusUpdate

logger = logging.getLogger("lms.audit")


class ApplicationService:
    def __init__(
        self,
        repository: ApplicationRepository,
        user_repo: UserRepository,
        product_repo: ProductRepository,
        repayment_repo: RepaymentRepository,
    ):
        self.repository = repository
        self.user_repo = user_repo
        self.product_repo = product_repo
        self.repayment_repo = repayment_repo

    def create_application(self, db: Session, payload: LoanApplicationCreate) -> LoanApplication:
        customer = self.user_repo.get(db, payload.user_id)
        if not customer:
            raise NotFoundError("Customer not found")
        if customer.role != UserRole.customer:
            raise ForbiddenError("Only customers can apply for loans")
        product = self.product_repo.get(db, payload.product_id)
        if not product:
            raise NotFoundError("Loan product not found")
        application = LoanApplication(
            user_id=payload.user_id,
            product_id=payload.product_id,
            requested_amount=payload.requested_amount,
            status=LoanStatus.pending,
        )
        with db.begin():
            return self.repository.create(db, application)

    def get_application(self, db: Session, application_id: int) -> LoanApplication:
        application = self.repository.get(db, application_id)
        if not application:
            raise NotFoundError("Loan application not found")
        return application

    def list_applications(self, db: Session, skip: int, limit: int) -> list[LoanApplication]:
        return self.repository.list(db, skip, limit)

    def update_status(self, db: Session, application_id: int, payload: LoanApplicationStatusUpdate) -> LoanApplication:
        application = self.get_application(db, application_id)
        officer = self.user_repo.get(db, payload.processed_by)
        if not officer:
            raise NotFoundError("Loan officer not found")
        if officer.role != UserRole.loan_officer:
            raise ForbiddenError("Only loan officers can approve or reject")

        if payload.status == LoanStatus.approved:
            product = self.product_repo.get(db, application.product_id)
            if application.requested_amount > product.max_amount:
                raise BadRequestError("Requested amount exceeds product maximum")
            requested_amount = application.requested_amount
            approved_amount = payload.approved_amount if payload.approved_amount is not None else requested_amount
            if approved_amount > product.max_amount:
                raise BadRequestError("Approved amount exceeds product maximum")
            application.approved_amount = approved_amount
            application.status = LoanStatus.approved
            application.processed_by = officer.id
            logger.info("Loan application %s approved by officer %s", application.id, officer.id)
        elif payload.status == LoanStatus.rejected:
            application.status = LoanStatus.rejected
            application.processed_by = officer.id
            logger.info("Loan application %s rejected by officer %s", application.id, officer.id)
        elif payload.status == LoanStatus.disbursed:
            if application.status != LoanStatus.approved:
                raise BadRequestError("Loan must be approved before disbursement")
            application.status = LoanStatus.disbursed
        elif payload.status == LoanStatus.closed:
            if application.approved_amount is None:
                raise BadRequestError("Loan must be approved before closing")
            total_paid = (
                db.query(func.coalesce(func.sum(Repayment.amount_paid), 0.0))
                .filter(Repayment.loan_application_id == application.id)
                .scalar()
            )
            if total_paid < application.approved_amount:
                raise BadRequestError("Loan cannot be closed before full repayment")
            application.status = LoanStatus.closed
        else:
            raise BadRequestError("Unsupported status transition")

        with db.begin():
            return self.repository.update(db, application)
