'''
Write a basic calculator program called calculator.py.
The user will enter:
The operation to perform
The first operand
The second operand
The operation is a string
The operands are floats

Valid operations are: add, sub, mul, div
The output will display up to 2 decimals.
'''

operation = input("Enter the operation: ")
operand_1 = float(input("Enter the first operand: "))
operand_2 = float(input("Enter the second operand: "))

if operation == "add":
    result = operand_1 + operand_2

elif operation == "sub":
    result = operand_1 - operand_2
elif operation == "mul":
    result = operand_1 * operand_2
elif operation == "div":
    result = operand_1 / operand_2

print("Result is", round(result, 2))

