from app.repositories.loan_repository import LoanRepository
from app.services.loan_service import LoanService

_loan_repository = LoanRepository()
_loan_service = LoanService(_loan_repository)


def get_loan_service() -> LoanService:
    return _loan_service
