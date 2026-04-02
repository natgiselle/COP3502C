'''
class Person:

# initialize the constructor instance of a. 

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def change_age(self, newage):
        self.age = newage

    def add_job(self, job):
        self.job = job
# initialize an instance of that class (an object)

p1 = Person("natbat", 19)
print(p1.age, p1.name) #<instance>.<attribute>

# if we have a function and its func(x,y) you can do print(initalizing the object (instance of the class).class_parameter) one at a time

p2 = Person("strawberry", 20) # doesnt need the p2 inside of it aince its already equaling to self (do need it when its just plugging in function)
print(p2.age, p2.name)



p1.change_age(99)
print(p1.age)

# can define an attribute even if it isnt in the initial constructor can add attributes as we go on
p1.job = "Teacher"
print(p1.job)


p1.add_job("Singer")
print(p1.job)
'''

class Student:
    '''
    pass
s1 = Student()
s1.name = "gigi"
s1.age = 5
s1.major = "biscuit making"
'''



# print(s1) # prints the Object ID: <__main__.Student object at 0x1051f1a90>
# always make sure to do <instance>.<class attribute>

# print(s1.name, s1.age, s1.major)

# can do one by one without constructor but is inefficient which is why we usde a constructor
    def __init__(self, age, name, major):
        self.age = age
        self.name = name
        self.major = major

s1 = Student(5, "gigi", "biscuit making")
print(s1.age, s1.name, s1.major)







