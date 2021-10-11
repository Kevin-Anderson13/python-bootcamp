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
    # @classmethod
    # def all_balances(cls):
    #     sum = 0
    #     # we use cls to refer to the class
    #     for account in cls.all_accounts:
    #         sum += account.balance
    #     return sum


# account_1 = BankAccount(.05, 100)
# print(account_1.int_rate)
# print(account_1.balance)

# account_2 = BankAccount()
# print(account_2.int_rate)
# print(account_2.balance)


# account_1.deposit(2000).deposit(3000).deposit(4000).withdraw(7000).yield_interest().display_account_info()
# account_2.deposit(2000).deposit(3000).withdraw(4000).withdraw(40000).withdraw(4000).withdraw(40000).yield_interest().display_account_info()

# print(BankAccount.all_balances())


class User:
    bank_name = "El Banko del Utah"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .01, balance = 0)

    def make_deposit(self):
        self.account.deposit()
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw()
        return self

    def display_user_balance(self):
        print(f"{self.name} has {self.account.balance} left in their bank account.")
        return self

    # def transfer_money(self, amount, other_user):
    #     self.account_balance -= amount
    #     other_user.account_balance += amount
    #     self.display_user_balance
    #     other_user.display_user_balance
    #     return self

kelsee = User("Kelsee Von Strucker", "kelsee@email.com")
kevin = User("Kevin Anderson", "kevin@email.com")
tyson = User("Tyson Galovich", "tyson@email.com")

print(kelsee.name)
print(kevin.name)
print(tyson.name)

kelsee.make_deposit(100000).make_deposit(1000000).make_deposit(1277000).make_withdrawl(1500000).display_user_balance()



# kevin.make_deposit(10).make_deposit(50).make_withdrawl(20).make_withdrawl(30).display_user_balance()



# tyson.make_deposit(5).make_withdrawl(1).make_withdrawl(1).make_withdrawl(1).display_user_balance()



# kelsee.transfer_money(800000, kevin)