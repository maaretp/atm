from atm import ATM, Account

def test_sufficient_balance_money_dispensed():
    atm = ATM()
    account = Account(300)
    assert account.withdraw(170, atm) == {100: 1, 50: 1, 20: 1}
    assert account.balance == 130

