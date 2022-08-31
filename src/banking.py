class BankAccount:

    def __init__(self):
        self.balance = 0
        self.name = None

    def deposit(self, gbp):
        self.balance = self.balance + gbp

    def set_name(self, name):
        self.name = name
