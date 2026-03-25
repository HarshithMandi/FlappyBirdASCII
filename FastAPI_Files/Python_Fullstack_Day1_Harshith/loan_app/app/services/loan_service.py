from app.core.config import config
from app.repositories.loan_repository import LoanRepository
from app.schemas.loan_schema import LoanCreate, LoanResponse, LoanStatusResponse


class LoanService:
    def __init__(self, loan_repository: LoanRepository) -> None:
        self.loan_repository = loan_repository

    def submit_application(self, payload: LoanCreate) -> LoanResponse:
        status = "PENDING"
        if payload.loan_amount > payload.income * config.eligibility_multiplier:
            status = "REJECTED"

        created = self.loan_repository.add_loan(
            {
                "applicant_name": payload.applicant_name,
                "income": payload.income,
                "loan_amount": payload.loan_amount,
                "status": status,
            }
        )
        return LoanResponse(**created)

    def get_application(self, loan_id: int) -> LoanResponse:
        loan = self.loan_repository.get_loan_by_id(loan_id)
        if loan is None:
            raise ValueError("Loan application not found")

        return LoanResponse(**loan)

    def list_applications(self) -> list[LoanResponse]:
        loans = self.loan_repository.list_loans()
        return [LoanResponse(**loan) for loan in loans]

    def approve(self, loan_id: int) -> LoanStatusResponse:
        loan = self.loan_repository.get_loan_by_id(loan_id)
        if loan is None:
            raise ValueError("Loan application not found")

        if loan["status"] != "PENDING":
            raise ValueError("Only pending loans can be approved")

        eligibility_limit = loan["income"] * config.eligibility_multiplier
        if loan["loan_amount"] > eligibility_limit:
            raise ValueError("Loan amount exceeds eligibility limit")

        updated = self.loan_repository.update_status(loan_id, "APPROVED")
        return LoanStatusResponse(
            message="Loan approved successfully", status=updated["status"]
        )

    def reject(self, loan_id: int) -> LoanStatusResponse:
        loan = self.loan_repository.get_loan_by_id(loan_id)
        if loan is None:
            raise ValueError("Loan application not found")

        if loan["status"] != "PENDING":
            raise ValueError("Only pending loans can be rejected")

        updated = self.loan_repository.update_status(loan_id, "REJECTED")
        return LoanStatusResponse(message="Loan rejected", status=updated["status"])
