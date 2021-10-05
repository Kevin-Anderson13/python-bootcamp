class User:
    bank_name = "El Banko del Utah"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.name} has {self.account_balance} left in their bank account.")

    # def transfer_money(self, other_user, amount):
    #     self.account_balance -= amount
    #     other_user.account_balance += amount

kelsee = User("Kelsee Von Strucker", "kelsee@email.com")
kevin = User("Kevin Anderson", "kevin@email.com")
tyson = User("Tyson Galovich", "tyson@email.com")

print(kelsee.name)
print(kevin.name)
print(tyson.name)

kelsee.make_deposit(100000)
kelsee.make_deposit(1000000)
kelsee.make_deposit(1277000)
kelsee.make_withdrawl(1500000)

kevin.make_deposit(10)
kevin.make_deposit(50)
kevin.make_withdrawl(20)
kevin.make_withdrawl(30)


tyson.make_deposit(5)
tyson.make_withdrawl(1)
tyson.make_withdrawl(1)
tyson.make_withdrawl(1)


print(kelsee.account_balance)
print(kevin.account_balance)
print(tyson.account_balance)

kelsee.display_user_balance()



