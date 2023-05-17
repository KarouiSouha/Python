class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        return self
    
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")    
            self.balance-=5
        return self    
    def display_account_info(self):
        print("Balance:$"+ str(self.balance))
        return self    
    def yield_interest(self):
        if(self.balance>0):
            self.balance+=self.balance*self.int_rate
            return self   

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
        
    def transfer_money(self, amount, other_user):
        self.account.balance = self.account.balance - amount
        other_user.account.balance = other_user.account.balance + amount 
        print(f"{self.name} just transferred {amount} dollars to {other_user.name}")
        return self

    def display_account_info(self):
        print(f"Name: {self.name}, {self.account.display_account_info()}")
        return self

user1 = User("Youssef","karoui.youssef17@gmail.com")
user2 = User("souha","karoui.souha18@gmail.com")

user2.account.deposit(300)
user2.display_account_info()
user1.account.deposit(2500)

user2.transfer_money(700,user1)
user1.account.deposit(200).withdraw(100).display_account_info()