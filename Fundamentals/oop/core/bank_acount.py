class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate=0.01
        self.balance=0
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
    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()    
bankaccount1=BankAccount(0.1,0)
bankaccount2=BankAccount(0.1,1000)
bankaccount1.deposit(200).deposit(400).deposit(1000).withdraw(1500).yield_interest().display_account_info()           
bankaccount2.deposit(10000).deposit(150000).withdraw(1500).withdraw(2000).withdraw(40).withdraw(6000).display_account_info() 
BankAccount.display_all_accounts()
