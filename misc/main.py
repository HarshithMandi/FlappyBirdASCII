from Bank_System.Accounts.savings import SavingsAccount
from Bank_System.Accounts.current import CurrentAccount
from Bank_System.Accounts.base_account import BankAccount   

SavingsAccount1= SavingsAccount("Alice", 1000, 0.05)
CurrentAccount1= CurrentAccount("Bob", 2000)

SavingsAccount1.calculate_interest()
CurrentAccount1.calculate_interest()
SavingsAccount1.display_info()
CurrentAccount1.display_info()