'''
class Employee:
    pay_raise = 0.2

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def increase_pay(self):
        self.pay += self.pay * pay_raise
        
rob = Employee("Rob", 100)
rob.increase_pay()
print(rob.pay)
'''

'''
class Employee:
    pay_raise = 0.2

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay


rob = Employee("Rob", 100)
andrew = Employee("Andrew", 200)
andrew.pay_raise = 0.4
print(Employee.pay_raise, rob.pay_raise, andrew.pay_raise)
'''

'''
class Shoes:
    count = 0

    def __init__(self, color):
        self.color = color
        Shoes.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


boot = Shoes('brown')
sneaker = Shoes('green')
Shoes.count += 1
print(Shoes.get_count())
'''

'''
class Student:
    def __init__(self, grade):
        self.grade = grade

    @staticmethod
    def increase_grade(student, grade):
        student.grade += 10
        grade = 92


sam = Student(86)
grade = 99
Student.increase_grade(sam, grade)
print(sam.grade + grade)
'''

'''
class Dog:
    def __init__(self, breed):
        self.breed = breed
        
    def __str__(self):
        return f"Woof! I am a {self.breed}"

dog = Dog("golden retriever")
print(dog)
'''

'''
class Counter:
    count = 0

    def __init__(self):
        self.count += 1

c1 = Counter()
c2 = Counter()

print(Counter.count)
'''

'''
class Data:
    values = []

    def __init__(self, number):
        self.values.append(number)

d1 = Data(10)
d2 = Data(20)
d3 = Data(30)

print(d1.values)
'''

# error
# 0.2 0.2 0.4
# 3
# 195
# Woof! I am a gollden retriever
# 0
# [10,20,30]