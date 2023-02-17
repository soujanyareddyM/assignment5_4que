class Account:                                            

    def _init_(self,title,AccountBalance):              
        self.title = None                        
        self.AccountBalance = 0                            

class SavingsAccount(Account):                          

    def _init_(self, title, AccountBalance,interestRate):      
        self.interestRate = interestRate
        super()._init_(title, AccountBalance)


        self.title = title                                 
        self.AccountBalance = AccountBalance

    def display(self):                                     
       return f"Name: {self.title}\nAccount Balance: {self.AccountBalance}\nInterest rate: {self.interestRate}"
    
    
obj = SavingsAccount("Demo",5000,7)
print(obj.display())