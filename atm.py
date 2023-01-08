class ATM:
    def __init__(self):
        self.euro_bills = {
            20: 1,
            50: 1,
            100: 1
        }

    def dispense(self, amount):
        if amount > 0:
            # check if sufficient balance is available in the ATM
            total_available_amount = sum([bill * self.euro_bills[bill] for bill in self.euro_bills])
            if amount > total_available_amount:
                return "Insufficient balance in the ATM"
            else:
                # check if the required amount can be dispensed using the available denominations
                amount_left = amount
                result = {}
                for bill in sorted(self.euro_bills.keys(), reverse=True):
                    while self.euro_bills[bill] > 0 and amount_left >= bill:
                        result[bill] = result.get(bill, 0) + 1
                        self.euro_bills[bill] -= 1
                        amount_left -= bill
                if amount_left > 0:
                    return "Required amount cannot be dispensed using the available denominations"
                else:
                    return result

class Account:
    def __init__(self, balance):
        self.daily_limit_per_account = 300
        self.balance = balance

    def withdraw(self, amount, atm):
        if (amount > self.daily_limit_per_account or amount > self.balance):
            return "Insufficient funds in account"
        else:
            result = atm.dispense(amount)
            if isinstance(result, dict):
                self.balance -= amount
                self.daily_limit_per_account -= amount
                return result
            else:
                return result

