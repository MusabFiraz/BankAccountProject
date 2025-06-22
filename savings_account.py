from BankClass import BankAccount

class SavingsAccount(BankAccount):
    def add_interest(self, interest_rate):
        interest = self.current_balance * interest_rate
        self.current_balance += interest
