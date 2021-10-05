class User:
    bank_name = "El Banko del Utah"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name} has {self.account_balance} left in their bank account.")
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



kevin.make_deposit(10).make_deposit(50).make_withdrawl(20).make_withdrawl(30).display_user_balance()



tyson.make_deposit(5).make_withdrawl(1).make_withdrawl(1).make_withdrawl(1).display_user_balance()



# kelsee.transfer_money(800000, kevin)