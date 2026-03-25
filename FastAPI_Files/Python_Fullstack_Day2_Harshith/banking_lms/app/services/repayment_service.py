from datetime import date

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import BadRequestError, NotFoundError
from app.models.loan_application import LoanStatus
from app.models.repayment import Repayment
from app.repositories.application_repository import ApplicationRepository
from app.repositories.repayment_repository import RepaymentRepository
from app.schemas.repayment_schema import RepaymentCreate


class RepaymentService:
    def __init__(self, repository: RepaymentRepository, application_repo: ApplicationRepository):
        self.repository = repository
        self.application_repo = application_repo

    def add_repayment(self, db: Session, payload: RepaymentCreate) -> Repayment:
        application = self.application_repo.get(db, payload.loan_application_id)
        if not application:
            raise NotFoundError("Loan application not found")
        if application.status not in {LoanStatus.approved, LoanStatus.disbursed}:
            raise BadRequestError("Repayments allowed only for approved or disbursed loans")
        if application.approved_amount is None:
            raise BadRequestError("Loan must have an approved amount before repayment")

        total_paid = (
            db.query(func.coalesce(func.sum(Repayment.amount_paid), 0.0))
            .filter(Repayment.loan_application_id == application.id)
            .scalar()
        )
        outstanding = application.approved_amount - total_paid
        if payload.amount_paid <= 0:
            raise BadRequestError("Repayment amount must be greater than zero")
        if payload.amount_paid > outstanding:
            raise BadRequestError("Repayment exceeds outstanding balance")

        repayment = Repayment(
            loan_application_id=payload.loan_application_id,
            amount_paid=payload.amount_paid,
            payment_date=payload.payment_date or date.today(),
            payment_status=payload.payment_status,
        )

        with db.begin():
            created = self.repository.create(db, repayment)
            new_total = total_paid + payload.amount_paid
            if new_total >= application.approved_amount:
                application.status = LoanStatus.closed
                self.application_repo.update(db, application)
            return created

    def list_repayments(self, db: Session, loan_application_id: int) -> list[Repayment]:
        return self.repository.list_by_application(db, loan_application_id)
