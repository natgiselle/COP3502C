# M10B In-Class Activities

'''
Secure Account

Write a class, SecureAccount, that inherits from the Account class to add a password.
All of the methods for SecureAccount take in a password as the final parameter.
If the password parameter does not match the password passed to the constructor,
the method should print “Incorrect password” and do nothing.

The Account class has the following methods:
__init__(self):
Create a new Account with a balance of 0
get_balance(self):
Returns the current account balance
deposit(self, amount):
Deposits amount dollars into the account
withdraw(self, amount):
Withdraws amount dollars from the account

The SecureAccount class has the following methods:
__init__(self, password):
Create a new SecureAccount with a balance of 0
get_balance(self, password):
Returns the current account balance
deposit(self, amount, password):
Deposits amount dollars into the account
withdraw(self, amount, password):
Withdraws amount dollars from the account
'''

class Account:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
class SecureAccount(Account):
    def __init__(self, password):
        super().__init__()
        self.password = password
    
    def get_balance(self, password):
        if self.password != password:
            print("Incorrect password")
            return
        return super().get_balance() 
    
    def deposit(self, amount, password):
        if self.password != password:
            print("Incorrect password")
            return
        return super().deposit(amount)
    
    def withdraw(self, amount, password):
        if self.password != password:
            print("Incorrect password")
            return
        return super().withdraw(amount)

acc = SecureAccount("password")
acc.get_balance("foo")
print(acc.get_balance("password"))
acc.deposit(5, "bar")
print(acc.get_balance("password"))
acc.deposit(5, "password")
print(acc.get_balance("password"))




'''
Memory Calculator
Write a class, MemoryCalculator, that inherits from the Calculator class.
The Calculator class allows adding and subtracting numbers.
The MemoryCalculator class stores the previous result and replaces any argument equal to “RESULT” with the previous result.
In the first calculation, the previous result is 0.

Methods for Calculator and MemoryCalculator:
__init__(self):
For MemoryCalculator, this should set the previous result to 0.
add(self, x, y):
Returns the sum of x and y
sub(self, x, y):
Returns the value of x minus y
Example:
calc = MemoryCalculator()
print(calc.add("RESULT", 2))
print(calc.add(3, "RESULT"))
print(calc.sub(15, "RESULT"))
'''
print()
print()
class Calculator:
    def __init__(self):
        pass
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y

class MemoryCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.prev_result = 0
    def add(self, x, y):
        if x == "RESULT":
            x = self.prev_result
        if y == "RESULT":
            y = self.prev_result
        self.prev_result = super().add(x,y)
        return self.prev_result

    def sub(self, x, y):
        if x == "RESULT":
            x = self.prev_result
        if y == "RESULT":
            y = self.prev_result
        self.prev_result = super().sub(x,y)
        return self.prev_result

calc = MemoryCalculator()
print(calc.add("RESULT", 2))
print(calc.add(3, "RESULT"))
print(calc.sub(15, "RESULT"))
'''
Fractions
Write a class, ImprovedFraction, that inherits from Fraction.
Fraction represents a fraction with a numerator and a denominator.
Improved Fraction adds several extra features to the Fraction class.

Fraction methods:
__init__(self, numerator, denominator)
Create a new fraction with the given numerator and denominator.
get_numerator(self)
Returns the fraction's numerator.
get_denominator(self)
Returns the fraction's denominator.
add(self, other)
Returns the sum of self and other. Self and other should both be fractions.
multiply(self, other)
Returns the product of self and other. Self and other should both be fractions.

ImprovedFraction methods:
add(self, other)
If other is an int N, add the fraction N/1 to self. Otherwise add the fractions using Fraction's add method.
multiply(self, other)
If other is an int N, multiply self by the fraction N/1. Otherwise multiply the fractions using Fraction's multiply method.
__add__(self, other)
Overloads the + operator to call the add method
__mul__(self, other)
Overloads the * operator to call multiply
__str__(self)
Overloads the str function to return a string of the format “numerator/denominator”
'''
print()
print()

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
    
    def add(self, other):
        # _a_  + _c_  =    __a*d_+_b*c__
        #  b      d            b*d
        a = self.numerator
        b = self.denominator
        
        c = other.numerator
        d = other.denominator

        return ImprovedFraction((a * d) + (b * c), (b * d))
    
    def multiply(self, other):
        a = self.numerator
        b = self.denominator
        
        c = other.numerator
        d = other.denominator
        return ImprovedFraction(a * c, b * d)
    
class ImprovedFraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
    
    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)  # convert int to fraction N/1
        return super().add(other)    # now always a fraction
    
    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)  # convert int to fraction N/1
        return super().multiply(other)    # now always a fraction
    
    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
print(ImprovedFraction(1, 2) + 5)
print(ImprovedFraction(3, 4) * 2)
