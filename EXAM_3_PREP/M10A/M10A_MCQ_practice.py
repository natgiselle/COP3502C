# QUESTION 1

class Student:
    def __init__(self, grade, major):
        self.grade = grade
        self.major = major
    def calc_grade(self):
        if self.major == "CS": 
           return self.grade // 10 # student1.calc_grade() is 90 // 10 = 9
        else:
           return self.grade // 5 # student2.calc_grde() is 100 // 5 = 20




student1 = Student(90, "CS")
student2 = Student(100, "ART")


print(student2.calc_grade() * student1.calc_grade()) # 20 * 9 = 180

# OUTPUT:
# B) 180

# QUESTION 2
class Gator:
    name = "Albert"

gator1 = Gator() # creates a Gator object
print(gator1.name, end=" ") # since there is no initializer (constructor) you csn create and assign attributes manually here and since there is no constructor the name variable in class Gator is the name for gator1 object
# gator1.name currently has value of "Albert"
Gator.name = "Alberta" # this changes the name variable of the Gator class to "Alberta"
print(gator1.name) # is now Alberta so it changes that instance of the class name to Alberta

# OUTPUT:
# Albert
# Alberta

# QUESTION 3
'''
class Parent:
    def __init__(self):
        self.value = 10
    def method(self):
        return self.value


class Child(Parent):
    def __init__(self):
        self.value = 20
    def method(): # ANY INSTANCE METHOD MUST HAVE SELF IN THE PARAMETERS it wouldve been 40 with method(self) in here
        return super().method() * 2


obj = Child()
print(obj.method())
'''
# OUTPUT:
# TypeError: Child.method() takes 0 positional arguments but 1 was given

# QUESTION 4
'''
class Animal():
    def __init__(self):
        self.name = ""
    def print(self):
        print("animal", end=" ")

class Cat(Animal):
    def print(self):
        print("cat", end=" ")

so cat(animal) did overright with print()
bcs it had it as print(self) in cat(animal)
but bcs dog didnt it just does print()
from the original making it just animal

class Dog(Animal):
    def woof(self):
        print("woof", end=" ")


animal = Animal() # creates Animal object (instance of Animal class)
cat = Cat() # creates a Cat object of Animal class
dog = Dog()
animal.print()
cat.print() # uses print(self) in Cat(Animal) so it overrrides it since cat class has print(self) as well and replaced with cat
dog.print() # doesnt use woof() so its just animal (DOES NOT OVERRIDE print() with dog HERE since it isnt in the Dog class!)
'''

# OUTPUT:
# animal cat animal     ********GOT IT WRONG ACCIDENTALY THOUGHT animal cat woof its not woof bcs it doenst do dog.woof()*********

# QUESTION 5

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"Book: {self.title} by {self.author}"

class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def get_info(self):
        return f"EBook: {self.title} by {self.author}, Size {self.file_size}MB"


digital_edition = Ebook('1984', 'George Orwell', 2)
print(digital_edition.get_info())

# OUTPUT:
# Ebook: 1984 by George Orwell, File Size: 2MB

# QUESTION 6

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


    def get_speed(self):
        return f"{self.name} speed: {self.speed}km/h"


class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type


    def get_car_info(self):
        return f"{self.get_speed()}, Fuel type: {self.fuel_type}"


car1 = Car("Toyota", 180, "Petrol")
print(car1.get_car_info())

# OUTPUT:
# Toyota speed: 180km/h, Fuel type: Petrol
