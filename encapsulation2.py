#Problem on the encapsulation method
class BankAccount:
    def __init__(self,holder_name,account_number,balance):
        self.holder_name = holder_name
        self.account_number = account_number 
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,amount):
        self.__balance = amount

    def deposite(self,amount):
        if(amount>0):
            self.__balance+=amount 
            print(f"{amount} credited!")
        else:
            print("Invalid Balance.")
    
    def withdraw(self,amount):
        if(amount<=self.__balance):
            self.__balance-=amount 
            print(f"{amount} debited.")
        else:
            print("Insufficient Balance")
    
    def details(self):
        print(f"Holder Name: {self.holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.__balance}")

class SavingsAccount(BankAccount):
    def __init__(self,holder_name,account_number,balance,interest):
        super().__init__(holder_name,account_number,balance)
        self.interest = interest 
    
    def add_interest(self):
        interest = self.balance*self.interest/100
        # self.deposite(interest)
        self.balance = self.balance+interest
    
    def details(self):
        super().details()
        print("Account type: Savings")
        print("Interest:",self.interest)

class CurrentAccount(BankAccount):
    def __init__(self,holder_name,account_number,balance,overdraft_limit):
        super().__init__(holder_name,account_number,balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self,amount):
        if(amount<=self.balance+self.overdraft_limit):
            self.balance = self.balance-amount
            print(f"{amount} debited")
        else:
            print("Insufficient balance")

    def details(self):
        super().details()
        print("Account Type: Current")
        print("Overdraft Limit:",self.overdraft_limit)




# sa = SavingsAccount("Manoj",1234567890,1000,5)
# sa.deposite(500)
# print(sa.balance)
# sa.add_interest()
# print(sa.balance)

ca = CurrentAccount("Deepak",1234567890,1000,500)
ca.deposite(1000)
print(ca.balance)
ca.withdraw(1000)
print(ca.balance)
ca.withdraw(1200)
print(ca.balance)
ca.withdraw(300)
print(ca.balance)
ca.deposite(500)
print(ca.balance)
ca.details()