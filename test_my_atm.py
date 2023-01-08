from atm import ATM, Account

def test_sufficient_balance_money_dispensed():
    atm = ATM()
    account = Account(300)
    assert account.withdraw(170, atm) == {100: 1, 50: 1, 20: 1}
    assert account.balance == 130

def test_this_scenario():
    atm = ATM()
    account = Account(300)
    assert account.withdraw(90, atm) == {50: 1, 20: 2}
    assert account.balance == 210
    assert account.withdraw(210, atm) == "Required amount cannot be dispensed using the available bills"
    assert account.balance == 210
    assert account.withdraw(200, atm) == {100: 2}
    assert account.balance == 10