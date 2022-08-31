class BankAccount:

    def __init__(self, name: str = None):
        self.balance = 0
        self.name = name

    def deposit(self, gbp):
        self.balance = self.balance + gbp