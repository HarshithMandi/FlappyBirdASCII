from exceptions import InsufficientFundsError
from base_account import BankAccount

class SavingsAccount(BankAccount):
    def interest(self):
        interest = self.balance * 0.04
        print(f"Interest earned: ${interest:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")