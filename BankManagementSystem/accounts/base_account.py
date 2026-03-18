from abc import ABC, abstractmethod
from datetime import datetime

class BankAccount(ABC):
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    @abstractmethod
    def interest_rate(self):
        pass

    def display_info(self):
        print("\n"+"="*30)
        print("GLOBAL BANK ACCOUNT INFORMATION")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("="*30)