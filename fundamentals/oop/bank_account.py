class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate = .01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if (self.balance - amount) < 0:
            print("Insufficient funds: Now I get to take $5 from you cause you messed up :).... Charging 5 dollar fee now.  Thank you! have a wonderful day......")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        return self

    # @staticmethod
    # def can_withdraw(balance,amount):
    #     if (balance - amount) < 0:
    #         return False
    #     else:
    #         return True

    # @classmethod
    # def change_bank_name(cls,name):
    #     cls.bank_name = name
    # # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum


account_1 = BankAccount(.05, 100)
print(account_1.int_rate)
print(account_1.balance)

account_2 = BankAccount()
print(account_2.int_rate)
print(account_2.balance)


account_1.deposit(2000).deposit(3000).deposit(4000).withdraw(7000).yield_interest().display_account_info()
account_2.deposit(2000).deposit(3000).withdraw(4000).withdraw(40000).withdraw(4000).withdraw(40000).yield_interest().display_account_info()

print(BankAccount.all_balances())
