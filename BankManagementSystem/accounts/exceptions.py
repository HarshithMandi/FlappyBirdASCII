class InsufficientFundsError(Exception):
    def __init__(self,balance,amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds: attempted to withdraw ${self.amount:.2f}, but balance is ${self.balance:.2f}"
        super().__init__(self.message)