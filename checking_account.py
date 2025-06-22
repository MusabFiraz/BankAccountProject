from BankClass import BankAccount

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        limit = 500  # max limit per transaction
        if amount > limit:
            print(f"Cannot withdraw more than ${limit} in one transaction.")
        else:
            super().withdraw(amount)
