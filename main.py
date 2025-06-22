from savings_account import SavingsAccount
from checking_account import CheckingAccount

# Create two savings accounts
s1 = SavingsAccount("Alice", 1000, 100, "SA123", "RT001")
s2 = SavingsAccount("Bob", 800, 100, "SA124", "RT002")

# Add interest
s1.add_interest(0.05)
s2.add_interest(0.03)

s1.print_customer_information()
print("-----")
s2.print_customer_information()

print("=====")

# Create two checking accounts
c1 = CheckingAccount("Charlie", 1200, 100, "CA123", "RT003")
c2 = CheckingAccount("Dana", 600, 100, "CA124", "RT004")

# Perform transactions
c1.withdraw(300)
c2.withdraw(600)  # should hit the transfer limit

c1.print_customer_information()
print("-----")
c2.print_customer_information()
