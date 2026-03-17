class InsufficientFundsError(Exception):
    """Raised when an account has insufficient funds for a transaction."""
    def __init__(self, message="Insufficient funds for this transaction."):
        self.message = message
        super().__init__(self.message)