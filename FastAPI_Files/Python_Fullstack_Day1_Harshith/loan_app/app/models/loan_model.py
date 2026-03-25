from dataclasses import dataclass


@dataclass(slots=True)
class LoanApplication:
    id: int
    applicant_name: str
    income: float
    loan_amount: float
    status: str
