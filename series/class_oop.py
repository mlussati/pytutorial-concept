class Account:
    def __init__(self, title=None, balance=0):
        # write your code here
        self.title = title
        self.balance = balance
        
    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdrawal(self, amount):
        self.balance = self.balance - amount

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        # write your code here
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        interestamount = (self.interestRate * self.balance)//100
        return interestamount
    
demo1 = SavingsAccount("Mark", 2000, 5)    
print(demo1.interestAmount())