from savings_account import SavingsAccount
from checking_account import CheckingAccount


def main():
    savings1 = SavingsAccount("Alice Johnson", "123456789", "987654321", 5000, 200, 2.5)
    savings2 = SavingsAccount("Bob Smith", "223456789", "887654321", 3000, 150, 3.0)

    savings1.apply_interest()
    savings2.apply_interest()

    checking1 = CheckingAccount("Charlie Brown", "323456789", "787654321", 2000, 100, 500)
    checking2 = CheckingAccount("Dana White", "423456789", "687654321", 1500, 50, 300)

    checking1.transfer(600, checking2)  # Should fail due to limit
    checking1.transfer(400, checking2)  # Should succeed

    savings1.print_customer_information()
    savings2.print_customer_information()
    checking1.print_customer_information()
    checking2.print_customer_information()


if __name__ == "__main__":
    main()
