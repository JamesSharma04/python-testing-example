from src.validation import validate_input

class BankAccount:

    def __init__(self):
        self.balance = 0
        self.firstname = None
        self.lastname = None

    def deposit(self, gbp):
        self.balance = self.balance + gbp

    def set_name(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def check_before_setting_name(self,firstname,lastname):
        if validate_input(firstname) and validate_input(lastname):
            return self.set_name(firstname,lastname)
        else:
            return False