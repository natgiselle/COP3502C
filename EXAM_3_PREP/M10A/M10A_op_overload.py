# Operator Overloading

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):  # converts object into a str format DOES NOT PRINT OBJECT ID
        return f"{self.name} is {self.age} years old"
    
p1 = Person("plankton", 1)
print(p1) # prints the object ID WITHOUT __str__ method 
# with __str__ method it prints the string returned 

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

b1 = Book("Java", 789)
b2 = Book ("C++", 456)
print(b1 == b2) # will always be false siince they are different instances of a class (different objects) 

b3 = b1
print(b1 == b3) # True because it is pointing to the same object

def __eq__(self, other): # overloaded the definition of this operstor based onour own requirements
    if not isinstance(other, Book):
        return False
    return self.title == other.title and self.isbn == other.isbn



class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def __lt__(self, other):
        if isinstance(self, Student): #  if there is an instance of student class (Student object)
            return self.name < other.name # use to define it by converting object into string format
        # return self.age < other.age
    def __str__(self):
        return f"{self.name} is {self.age} years old and majoring in {self.major}!"
s1 = Student("gru", 38, "mechanical engineering")
s2 = Student("kevin", 10, "business")
s3 = Student("stuart",9,"marketing")
students = [s1, s2, s3]
students.sort() # cannot evaluate unlesss you use __lt__ not supported since it must define what exactly we are sorting

for s in students:
    print(s)

# PREDICT THE OUTPUT

class Stud:
    pass

class Monster:
    def __init__(self, level=1, name="Monster"):
        self.level = level
        self.name = name

    def __eq__(self, other):
        print("Hi")
        if isinstance(other, Monster): # if there is an instance of other and monster that are based on def __eq__!! if there is instance of other and mOnster that is equal
            return True
        return 123 # they are not

# OUTPUT:
# Hi
# 123