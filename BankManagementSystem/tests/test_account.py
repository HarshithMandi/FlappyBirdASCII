import unittest
from accounts.current import CurrentAccount
from accounts.savings import SavingsAccount
from accounts.exceptions import InsufficientFundsError

class TestBankAccounts(unittest.TestCase):
    def setUp(self):
        self.current_account = CurrentAccount("John Doe", 1000)
        self.savings_account = SavingsAccount("Jane Doe", 2000)

    def test_savings_interest(self):
        expected_interest = 1000 * 0.04
        self.assertEqual(expected_interest,40.00)
    
    def test_current_interest(self):
        initial_balance = self.current_account.balance
        self.current_account.interest_rate()
        self.assertEqual(initial_balance, self.current_account.balance)
    
    def test_inheritance(self):
        self.assertEqual(self.current_account.name, "John Doe")
        self.assertEqual(self.savings_account.name, "Jane Doe")
    
    def test_InsufficientFundsError(self):
        acc= SavingsAccount("Alice", 100)
        with self.assertRaises(InsufficientFundsError) as context:
            acc.withdraw(150)

if __name__ == '__main__':
    unittest.main()