class Person:

    # constructor
    # parameters not always needed when making a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def change_age(self, new_age):
        self.age = new_age
        # doesnt have to return anything since it is UPDATING self.age directly
# establish outside of the class

# can also create an instance of a class and immediately call for its attribute within the same line
# can do this formula: <instance of class>.<attribute>
# put the parameters by not puting self if needs input
# for example:
# input name, age only even if constructor has self, name, age
# self is to be able to identify it is THAT object (instance of a class)
age_1 = Person("hi", 10).age
print(age_1)
p = Person("nat", 19)
print(p.age)
p.change_age(67)
print(p.age)

class Student_1:
    pass
s1 = Student_1()
# can also create new attributes by initalizing it to the object directly without constructor
s1.name = 'squidward'
s1.year = 3
s1.major = 'music'
s1.groceries = {'clarinet': 3, 'fish': 10, 'strawberries': 29}
print(s1.groceries)

class Student_2:
    def __init__(self, name, year, major, groceries):
        self.name = name
        self.year = year
        self.major = major
        self.groceries = groceries

s1 = Student_2("spongebob", 1, "jellyfish studies", {"snail bites for gary": 5, "bubbles": 2, "pants": 1})
print()
print(s1.name)
print(s1.year)
print(s1.major)
print(s1.groceries)

class Monster:
    def __init__(self, level = 1, name = "Monster"): # defaults, if you do it for one atritbute to be set to default you must do it to ALL
        self.level = level
        self.name = name

    def increase_level(self, amount):
        self.level += amount
    
m1 = Monster(100, 'mikewazowski')
m1.increase_level(40)
print(m1.level)



