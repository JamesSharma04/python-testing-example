from src.banking import BankAccount

def test_deposit_an_amount_into_the_account():
    # Given a bank account
    BankAccount.bank_account = BankAccount()

    # When I deposit 100 GBP into the bank account
    BankAccount.bank_account.deposit(100)

    # Then the bank account balance should be 100 GBP.
    assert BankAccount.bank_account.balance is 100

def test_bank_account_has_a_name():
    # Given a bank account
    BankAccount.bank_account = BankAccount()

    # When I set the bank account name to "John Doe"
    BankAccount.bank_account.set_name("John Doe")

    # Then the bank account name should be "John Doe"
    assert BankAccount.bank_account.name is "John Doe"
    