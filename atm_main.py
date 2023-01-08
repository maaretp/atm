from atm import ATM, Account

atm = ATM()
account = Account(300)

while True:
    withdraw_amount_str = input("Enter the amount you want to withdraw: ")
    if withdraw_amount_str.isdigit():
        withdraw_amount = int(withdraw_amount_str)
    else:
        print("Invalid input. Please enter a valid integer.")
    bills = account.withdraw(withdraw_amount, atm)
    print("Bills dispensed: ", bills)
    print("Account balance: ", account.balance)