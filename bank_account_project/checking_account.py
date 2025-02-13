from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, account_number, routing_number, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, account_number, routing_number, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit  # Max transfer per transaction

    def transfer(self, amount, recipient):
        if amount > self.transfer_limit:
            print(f"Transfer failed. Maximum transfer limit is ${self.transfer_limit}.")
        elif amount > 0 and self.get_balance() - amount >= self._BankAccount__minimum_balance:
            self.withdraw(amount)
            recipient.deposit(amount)
            print(f"Transferred ${amount} to {recipient.customer_name}.")
        else:
            print("Invalid transfer amount or insufficient funds.")
