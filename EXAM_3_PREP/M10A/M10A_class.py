# M10 In-Class Activities

'''
Pakuri
Write a class, Pakuri, representing a mythical creature used for combat. The class will have the following methods:
__init__(self, name)
Create a new Pakuri, with the specified name
attack(self, attack_name)
print out the message “{pakuri_name} used {attack_name}!”
speak(self)
Print out the message “{pakuri_name}, {pakuri_name}!”
'''
class Pakuri:
    def __init__(self, name):
        self.name = name

    def attack(self, attack_name):
        print(f"{self.name} used {attack_name}!")

    def speak(self):
        print(f"{self.name}, {self.name}!")

pikabu = Pakuri("Pikabu")
pikabu.speak()
pikabu.attack("thunderbolt")

'''
Bank Account
Write a class, BankAccount, representing a bank account. The class will have the following methods:
__init__(self)
Create a new bank account with a starting balance of 0
deposit(self, amount)
If amount is negative, print “Invalid amount.”
Otherwise, print “Deposited ${amount}” and add amount to balance
withdraw(self, amount)
If amount is negative, print “Invalid amount.”
If amount is greater than balance, print “You don't have enough money :(”
Otherwise, print “Withdrew ${amount}” and subtract amount from balance
display(self)
Prints a string “Current balance: ${balance}”.
'''
class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        if amount >= 0:
            print(f"Deposited ${amount}")
            self.balance += amount
        else:
            print(f"Invalid amount.")
    
    def withdraw(self, amount):
        if amount < 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("You don't have enough money :(")
        else:
            print(f"Withdrew ${amount}")
            self.balance -= amount
    def display(self):
        print(f"Current balance: ${self.balance}")
    
account = BankAccount()
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

'''
Coordinates
Write a class, Coordinate, representing a coordinate pair on the 2D plane. The class will have the following methods:
__init__(self, x, y)
Create a new coordinate with the given x and y
__eq__(self, other)
Overloads the == operator. Determines if two coordinates are equal to each other. Coordinates are equal if both their x and y values are the same.
__add__(self, other)
Overloads the + operator. Add two coordinates to create a new coordinate. The new coordinate's x is the sum of the original x values and the new coordinate's y is the sum of the original y values.
This should return a new Coordinate. It should not modify self or other
__str__(self)
Overloads the str() function. Returns a string of the form "(x, y)".

'''
class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x},{self.y})"

p1 = Coordinate(2, 4)
p2 = Coordinate(3, 7)
p3 = Coordinate(2, 4)
p4 = p1 + p2
print("p1 == p2?", p1 == p2)
print("p1 == p3?", p1 == p3)
print(f"{p1} + {p2} = {p4}")
print(p1)
