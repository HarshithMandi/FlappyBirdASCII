from app.core.storage import storage


class LoanRepository:
    def add_loan(self, loan_data: dict) -> dict:
        loan = loan_data.copy()
        loan["id"] = storage.loan_id_counter
        storage.loan_id_counter += 1
        storage.loans.append(loan)
        return loan

    def get_loan_by_id(self, loan_id: int) -> dict | None:
        for loan in storage.loans:
            if loan["id"] == loan_id:
                return loan
        return None

    def list_loans(self) -> list[dict]:
        return list(storage.loans)

    def update_status(self, loan_id: int, status: str) -> dict | None:
        loan = self.get_loan_by_id(loan_id)
        if loan is None:
            return None
        loan["status"] = status
        return loan
