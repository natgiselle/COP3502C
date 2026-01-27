# Write a python program that takes two numbers as input ans swaps their values
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

# How to swap two variables withot creating a third and without classifying both variables on the same line
num_1 = num_2 + num_1
num_2 = num_1 - num_2
num_1 = num_1 - num_2

print("After swapping: First number = ", num_1, "Second number = ", num_2)