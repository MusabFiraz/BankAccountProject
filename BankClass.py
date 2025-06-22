class BankAccount:
    # Class attribute
    bank_title = "Unity Trust Bank"

    # Constructor method
    def __init__(self, name, balance, minimum, account_number, routing_number):
        self.customer_name = name
        self.current_balance = balance
        self.minimum_balance = minimum
        self._account_number = account_number       # Protected
        self.__routing_number = routing_number      # Private

    # Deposit method
    def deposit(self, amount):
        self.current_balance = self.current_balance + amount

    # Withdraw method with basic check
    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Cannot withdraw, minimum balance would be too low.")
        else:
            self.current_balance = self.current_balance - amount

    # Print info method
    def print_customer_information(self):
        print("Bank:", BankAccount.bank_title)
        print("Name:", self.customer_name)
        print("Balance:", self.current_balance)
        print("Minimum Balance:", self.minimum_balance)
        print("Account Number:", self._account_number)

# Create two accounts
account1 = BankAccount("Alice", 300, 100, "A123", "R001")
account2 = BankAccount("Bob", 200, 50, "B456", "R002")

# Use the methods
account1.deposit(100)
account1.withdraw(250)
account1.print_customer_information()

print("-----")

account2.withdraw(180)
account2.deposit(50)
account2.print_customer_information()

