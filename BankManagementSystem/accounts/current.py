from base_account import BaseAccount

class CurrentAccount(BaseAccount):
    def interest_rate(self):
        print("Current accounts do not earn interest.")