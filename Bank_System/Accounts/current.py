from base_account import BankAccount

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current accounts do not earn interest.")