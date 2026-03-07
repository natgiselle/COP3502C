'''
def mystery1(n):
    def inner(n, a, b, c, d, e):
        if n <= 0:
            return a
        return inner(n - 1, b, c, d, e, a-c+e)
    return inner(n, 1, 2, 3, 4, 5)

print(mystery1(0))
print(mystery1(1))
print(mystery1(2))
print(mystery1(3))
print(mystery1(4))
print()
print(mystery1(5))
print(mystery1(6))
print(mystery1(7))
print(mystery1(8))
print(mystery1(9))
'''

def mystery1(n):
    a,b,c,d,e = 1,2,3,4,5
    for i in range(n):
        temp = a - c + e
        a = b
        b = c
        c = d
        d = e
        e = temp
    return a

# print(mystery1(5))
'''
make this same function but using recursion instead of a loop
def mystery2(number): # takes number adds the digits together returning the sum
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

print(mystery2(123))
'''

def mystery2(number):
    if number > 0:
        digit = number % 10
        return digit + mystery2(number // 10)
    else:
        return 0

