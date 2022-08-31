from src.banking import BankAccount

def test_deposit_an_amount_into_the_account():
    # Given a bank account
    BankAccount.bank_account = BankAccount()

    # When I deposit 100 GBP into the bank account
    BankAccount.bank_account.deposit(100)

    # Then the bank account balance should be 100 GBP.
    assert BankAccount.bank_account.balance is 100

def test_account_name_validation():
    # Given a bank account 
    BankAccount.bank_account = BankAccount()

    # when I check the name before setting it
    BankAccount.bank_account.check_before_setting_name("John", "Doe")

    # Then the bank account name should be "John Doe"
    assert BankAccount.bank_account.firstname is "John" 
    assert BankAccount.bank_account.lastname is "Doe"

def test_account_name_validation_fails_when_first_name_is_empty():
    # Given a bank account 
    BankAccount.bank_account = BankAccount()

    # when I check the name before setting it, then the name should not be set 
    assert BankAccount.bank_account.check_before_setting_name("", "Doe") is False

def test_account_name_validation_fails_when_last_name_is_empty():
    # Given a bank account 
    BankAccount.bank_account = BankAccount()

    # when I check the name before setting it, then the name should not be set 
    assert BankAccount.bank_account.check_before_setting_name("John", "") is False