class BankAccount:
    bank_title = "National Bank"

    def __init__(self, customer_name, account_number, routing_number, current_balance, minimum_balance):
        self.customer_name = customer_name
        self._account_number = account_number  # Protected
        self._routing_number = routing_number  # Protected
        self.__current_balance = current_balance  # Private
        self.__minimum_balance = minimum_balance  # Private

    def deposit(self, amount):
        if amount > 0:
            self.__current_balance += amount
            print(f"{self.customer_name} deposited ${amount}. New balance: ${self.__current_balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__current_balance - amount >= self.__minimum_balance:
                self.__current_balance -= amount
                print(f"{self.customer_name} withdrew ${amount}. New balance: ${self.__current_balance}")
            else:
                print(f"Insufficient funds. Minimum balance: ${self.__minimum_balance}")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__current_balance

    def print_customer_information(self):
        print("\nCustomer Information:")
        print(f"Bank: {self.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self._routing_number}")
        print(f"Current Balance: ${self.__current_balance}")
        print(f"Minimum Balance: ${self.__minimum_balance}")
        print("-" * 30)
