# M10A EXAMPLE QUESTIONS


# QUESTION 1
'''
class Circle:
    pi = 3.14 # PI is NOT DEFINED
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2 # MUST BE SELF.pi turned into attribute in constructor OR establish the value within the function
        
c = Circle(2)
print(c.area())
'''

# OUTPUT:
# name 'pi' is not defined. Did you mean: 'self.pi'?
# Error

# QUESTION 2
class MyClass:
    x = 9
    def __init__(self, x=2,y=1):
        self.y = y
        self.x = x
    def sum_nums(self):
        self.y += self.x
        return self.y

m = MyClass(4) # only has one positional arg presented but since there is default values established in the constructor then now x=4 but the y that wasnt inputted wil now assign default value for y=1
print(m.sum_nums())

# QUESTION 3
class Monster:
    count = 0
    def __init__(self, health):
        self.health = health
        self.count += 1 # default is zero established in clas since its self.count it takes from count = 0 0 +1 CANNOT DO IT IF ITS WITHOUT SELF
    @classmethod
    def get_count(cls): # can be ignored is not called in 
        return cls.count

m1 = Monster(1)
m2 = Monster(3) # health 3 count for that object (self.count) is plus 1 o 0 + 1

print(m2.count, Monster.count) # health isnt asked for, count for class default monster is just 0 for the class so 1 0 

# OUTPUT:
#  1 0

# QUESTION 4
class Monster2:
    def __init__(self, health):
        self.health = health
    @staticmethod
    def increase_health(monster, health):
        monster.health += 20 # m has health of 10 so tis is doing self.health += 20 basicaly which is 10 + 20 = 30
        health = 40 #not self.health therefore doesnt do anything

m = Monster(10)
health = 30 # is whats being used for the print not the one in the scope of the function 
Monster.increase_health(m, health)
print(m.health, health) # health of m which is the instance of Monster2 class

# OUTPUT:
# 30 30

# QUESTION 5
class Parent:
    def __init__(self, x, y=3): # is ALLOWED, if default is assigned must be assigned for all or if not it must be only the trailing ones near end 
        self.x = x
        self.y = y
class Child(Parent):
    def __init__(self, a, b):
        super().__init__(a) # inherits attribute x from Parent with a and not y so y=3 b=7 x=5
        self.b = b 

c = Child(5,7)
print(c.b ,c.x, c.y)
# 7 5 3
