#Decimal to Binary Conversion
'''
Write a function bin, that converts a decimal (base-10) 
number to its binary (base-2) representation. 
The function should take an integer as input and 
return a string containing the binary representation.


Examples:
Code on the left is the function call, 
code on the right is what is returned.
'''
'''


for each element in the str

if it isnt divisible by 2 its 1 
if its divisble by 2 and has no remainder its 0

'''

def bin(num):
    if num == 0:
        return '0'
    result = ""
    while num != 0:
        digit = str(num % 2)
        result = digit + result
        number //= 2
    return result

def capitalize(str):
    result = ""
    word_start = True
    for char in str:
        if word_start and char.lower() not in "ousnd":
            result += char.upper()
        else:
            result += char.lower()
        word_start = char == " "
    return result

def partition(nums, size):
    result = []
    for i in range(0, len(nums), size):
        result.append(nums[i:i + size])
    return result