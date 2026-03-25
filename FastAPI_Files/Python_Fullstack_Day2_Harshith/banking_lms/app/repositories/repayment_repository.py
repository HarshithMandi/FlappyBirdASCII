from sqlalchemy.orm import Session

from app.models.repayment import Repayment


class RepaymentRepository:
    def create(self, db: Session, repayment: Repayment) -> Repayment:
        db.add(repayment)
        db.flush()
        return repayment

    def list_by_application(self, db: Session, loan_application_id: int) -> list[Repayment]:
        return (
            db.query(Repayment)
            .filter(Repayment.loan_application_id == loan_application_id)
            .order_by(Repayment.payment_date.asc())
            .all()
        )
