from atm import ATM, Account, LimitError, FundsError, BillsError, BalanceError

atm = ATM()
account = Account(300)

bills = ""

while True:
    withdraw_amount_str = input("Enter the amount you want to withdraw: ")
    if withdraw_amount_str.isdigit():
        withdraw_amount = int(withdraw_amount_str)
    elif (withdraw_amount_str == "exit"):
        break
    else:
        print("Invalid input. Please enter a valid integer.")
    try:
        bills = account.withdraw(withdraw_amount, atm)
    except (LimitError, FundsError, BillsError, BalanceError) as e:
        print("Error: ", e)
        if BillsError: 
            bills = ""
    finally:
        print("Bills dispensed: ", bills)
        print("Account balance: ", account.balance)
