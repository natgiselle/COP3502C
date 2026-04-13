
# FRQ 1
'''
Prompt:
You are asked to create an airport logbook that stores information
about an airplane and the time it landed at the airport.

You will design two classes: Airplane Class, and AirportLog Class
The Airplane class will create an object constructed with the airplane's model, and capacity.

The AirportLog class will store many airplane objects inside of a dictionary called logbook,
with the key being the time, and the value being a list of airplane objects.

Inside the AirportLog class create a function add_airplane(time, model, capacity),
where time is a number and model and capacity will be used to create an airplane object.
Add the airplane to the logbook . Also create a print_airplanes_at_time(time)
that will print all the airplane models at the time passed in.
You do not need to create a main() function, only develop the classes.
'''
'''
class Airplane:

    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity
class AirportLog:
    def __init__(self):
        self.logbook = {}
        # dictionary where key is time, value is list of airplane objects do .append to each
    def add_airplane(self, time, model, capacity):
        plane = Airplane(model, capacity)
        if time not in self.logbook:
            self.logbook[time] = [] # time keyits value will be 
        self.logbook[time].append(plane)
    def print_airplanes_at_time(self, time):
        for airplane in self.logbook[time]:
            print(airplane.model, end= " ")

port = AirportLog()
port.add_airplane(1, "delta", 40)
port.add_airplane(1, "disney", 100)
port.print_airplanes_at_time(1) # delta disney

port = AirportLog()

port.add_airplane(1, "delta", 40)
port.add_airplane(2, "disney", 100)
port.add_airplane(3, "world", 100)
port.add_airplane(3, "hello", 100)
print()
port.print_airplanes_at_time(3) # world hello
'''



# FRQ 2
'''
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self): # all instance methods must use self inside!!!!
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, miles_per_gallon):
        super().__init__(make, model, year)
        self.miles_per_gallon = miles_per_gallon
    def display_info(self):
        super().display_info()
        print(f"Miles Per Gallon: {self.miles_per_gallon}")

new_vehicle = Vehicle("Toyota", "Camry", 2010)
new_vehicle.display_info()
print()
new_car = Car("Toyota", "Rav4", 2015, 26)
new_car.display_info()
'''
# @classmethod operates on the class level
# @staticmethod NO access to class or instance just a regular function

# FRQ 3

class Book:
    count = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = Book.count + 1 # because book_id is supposed to auto increment
        Book.count += 1

    def get_info(self):
        return f"ID: {self.book_id}, Title:{self.title}, Author: {self.author}"
    
    @classmethod
    def get_num_books(cls):
        return cls.count # think of cls as the self. but for classmethod specifically the class's count variable
    
    @staticmethod
    def is_classic(title): # means it doesnt pertain to anything with class just takes in an input and uses it (think like its a regular function)
            return 'a' in title.lower() # asks if blank is IN something never forget in is a keyword thing like if or not and
        
class FictionBook(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre
    
    def get_info(self):
        return f"{super().get_info()}, Genre: {self.genre}"
    
class NonFictionBook(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject

    def get_info(self):
        return f"{super().get_info()}, Subject: {self.subject}"

# Test Case 1:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(book1.get_info())
book2 = Book("The Hunger Games", "Suzanne Collins")
print(book2.get_info())
print("Number of Books:", Book.get_num_books())

# Test Case 2:
fiction_book1 = FictionBook("1984", "George Orwell", "Dystopian")
print(fiction_book1.get_info())
print("Is Classic:", Book.is_classic(fiction_book1.title))

# Test Case 3:
nonfiction_book1 = NonFictionBook("A Brief History of Time", "Stephen Hawking", "Science")
print(nonfiction_book1.get_info())
print("Is Classic:", Book.is_classic(nonfiction_book1.title))


# FRQ 4
class Student:
    def __init__(self, name, savings, college):
        self.name = name
        self.savings = savings
        self.college = college  
    
    def pay_tuition(self):
        if self.savings >= 20_000:
            self.savings -= 20_000
            print("You have successfully paid your tuition!")
        else:
            print('You do not have enough savings to pay your tuition.')
    
    def print(self):
        print()
        print(f"Student Name: {self.name}")
        print(f"Student Savings: {self.savings}")
        print(f"Student University: {self.college}")

student = Student("Tonya", 20000, "UF")
student.pay_tuition()
student.pay_tuition()
student.print()

# FRQ 5
class ToDoList:
    def __init__(self):
        self.todo_list= {}

    def add_task(self, task):
            self.todo_list[task] = False

    def complete_task(self, task):
        if task in self.todo_list:
            self.todo_list[task] = True
        else:
            print(f"Task '{task}' not found.")

    def display_tasks(self):
        print("Tasks:")
        for task, completed in self.todo_list.items():
            status = "Completed" if completed else "Not Completed"
            print(f"- {task}: {status}")

my_todo_list = ToDoList()
my_todo_list.add_task("Buy groceries")
my_todo_list.add_task("Wash the car")
my_todo_list.display_tasks()
my_todo_list.complete_task("Buy groceries")
my_todo_list.display_tasks()
