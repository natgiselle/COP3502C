# === Question 1 ===
"""
class A:
    def __init__(self, x):
        self.x = x
    def display(self):
        print("Class A")

class B(A):
    def __init__(self, y):
        super().__init__(y * 2)
    def display(self):
        print("Class B")

class C(B):
    def display(self):
        super().display()
        print("Class C")

obj = C(4)
obj.display()
print(obj.x)
"""


# === Question 2 ===
"""
class Cat:
    legs = 4

    def __init__(self, breed, food):
        self.breed = breed
        self.food = food

    def meow(self):
        print("Meow")

class Tabby(Cat):
    fur = "brown"

    def meow(self):
        print("Tabby Meow")

kyo = Cat("American Shorthair", "fish")
lego = Tabby("Tabby", "turkey")
kyo.meow()
lego.meow()
"""

# === Question 3 ===
"""
class Rectangle:
    def __init__(self, length = 4, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, s_length):
        super().__init__(s_length - 1, s_length + 1)
        self.s_length = s_length

s = Square(5)
print(s.s_length, s.length, s.width)
"""

# === Question 4 ===
"""
class Base:
    def __init__(self, a=2):
        self.a = a

class Derived(Base):
    def __init__(self, b):
        super().__init__()
        self.b = b

d = Derived(4)
print(d.a, d.b)
"""

'''
Class B
Class C 
8

Meow
Tabby Meow

ERROR

2 4

O(n)

The worst-case time complexity of an algorithm 
'''