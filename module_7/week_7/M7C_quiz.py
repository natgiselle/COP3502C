'''
def func(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return func(n // 2)
    return func(n // 2) + func(n // 2 + 1)

print(func(11))
'''

'''
def mystery(a, b):
    if b == 0:
        return a
    return mystery(b, a % b)

print(mystery(12, 18))
'''

'''
def mystery(s):
    if len(s) <= 1:
        return s
    return s[-1] + mystery(s[:-1])

print(mystery("hello"))
'''

'''
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))
'''

def mysterious(arr, size, target):
    if size == 1:
        if arr[0] >= target:
            return 1
        else:
            return 0
    if arr[size - 1] >= target:
        return mysterious(arr, size - 1, target) + 1
    else:
        return mysterious(arr, size - 1, target)

a = [3, 12, 9, 5, 10]
print(mysterious(a, len(a), 9))