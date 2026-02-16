# Sum
'''
Write a function, sum, that will take any number of arguments and return their sum:
With 0 arguments, sum should return 0.0
All arguments will be floats and the function will always return a float

Examples:
Code on the left is the function call, code on the right is what is returned.

sum()                           0.0
sum(1.0)                        1.0
sum(1.0, 2.0, 3.0, 4.0)         10.0
sum(0.5, 0.25, 0.125, 0.0625)   0.9375
sum(-2.5, 2.5, -1.0, 0.5, 0.5)  0.0
'''

# CREATES TUPLE OF SUMS AND RETURNS ADDITION OF EACH ITEM IN THE TUPLE
# Treat it like a list
def sum(*nums):
    value = 0.0
    for num in nums:
        value+=num
    return value
sum()

'''
Write a function, print_range, that takes two integer arguments and prints all the numbers between them.
Both arguments will always be ints
The first argument will always be smaller than the second argument
All numbers should be printed on the same line, separated by commas
The function should return nothing

Your output should end with a newline.
'''
def print_range(int1, int2):
    print(int1, end = "")
    for num in range(int1 + 1, int2 + 1):
        print(", ", end = "")
        print(num, end ="")
    print()
print_range(1, 3)

# Sum Digits
'''
Write a function, sum_of_digits, that will sum all the digits of a number. 
The function will take one parameters:
The number (an int)
This function will return an int

Examples:
Code on the left is the function call, code on the right is what is returned.

sum_of_digits(0)           0
sum_of_digits(5)           5
sum_of_digits(1234567)     28
sum_of_digits(765434567)   47
'''

# My answer
def sum_digits(digits):
    total = 0
    str_digits = str(digits)
    i = len(str_digits) - 1
    while i >= 0:
        chr = str_digits[i]
        chr = int(chr)
        total+=chr
        i-=1
    return total
print(sum_digits(765434567))

# The class example answer (another example)
'''
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number %10
        total = total + digit
        number = number // 10
    return total
'''