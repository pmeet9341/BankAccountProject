from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, account_number, routing_number, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, account_number, routing_number, current_balance, minimum_balance)
        self.interest_rate = interest_rate  # % annual interest rate

    def apply_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} applied at {self.interest_rate}% rate.")
