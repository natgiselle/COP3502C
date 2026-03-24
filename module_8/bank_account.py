class BankAccount:
    def __init__(self):
        self.balance = 0 # create a new bank account with a starting balance of 0

    def deposit(self, amount):
        if amount < 0: # when amount is negative
            print("Invalid amount.")
        else:
            print(f"Deposited ${amount}")
            self.balance += amount # adds amount to balance
    
    def withdraw(self, amount):
        if amount < 0: # when amount is negative
            print("Invalid amount.")
        elif amount > self.balance: # amount is greater than balance
            print("You don't have enough money :(")
        else:
            print(f"Withdrew ${amount}")
            self.balance -= amount # subtract amount from balance

    def display(self):
        print(f"Current balance: ${self.balance}")

account = BankAccount() # initalizes an object of BankAccount class
account.display()
account.deposit(-1)
account.deposit(10)
account.display()
account.withdraw(20)
account.withdraw(-5)
account.withdraw(1)
account.display()
account.withdraw(9)
account.display()


