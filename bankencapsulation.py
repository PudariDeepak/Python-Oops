#Encpsultion in the bank account
class Bankaccount:
    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Amount must be positive")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawl amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawl successful")

account = Bankaccount("Deepak",5000)

print(account.get_balance())
account.deposit(2000)
print(account.get_balance())
account.withdraw(5000)
print("Available Balance:",(account.get_balance()))