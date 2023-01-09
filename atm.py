class Account:
    def __init__(self, balance):
        self.daily_limit_per_account = 300
        self.balance = balance

    def withdraw(self, amount, atm):
        if (amount <= 0 or not isinstance(amount, int)):
            raise ValueError("Invalid amount")
        elif (amount > self.balance):
            raise FundsError("Insufficient funds in account")
        elif (amount > self.daily_limit_per_account):
            raise LimitError("Daily withdrawal limit reached")
        try:
            result = atm.dispense(amount)
            self.balance -= amount
            self.daily_limit_per_account -= amount
        except (BillsError, BalanceError) as e:
            raise e
        return result


class ATM:
    def __init__(self):
        self.euro_bills = {
            20: 2,
            50: 1,
            100: 3
        }

    def dispense(self, amount):
        if amount > 0:
            # check if sufficient balance is available in the ATM
            total_available_amount = sum([bill * self.euro_bills[bill] for bill in self.euro_bills])
            print(str(total_available_amount) + "Extra")
            if amount > total_available_amount:
                raise BalanceError("Insufficient money to give out in the ATM")
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
                    raise BillsError("Required amount cannot be dispensed using the available bills")
                return result




class LimitError(Exception):
    pass

class FundsError(Exception):
    pass

class BillsError(Exception):
    pass

class BalanceError(Exception):
    pass