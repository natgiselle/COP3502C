'''def F(n):
    i = 0
    while n>=0:

    return int'''

'''def fourbonacci(n):
    a,b,c,d = 1,4,7,8
    for i in range (n-1):
        temp = a*4+b*3+c*2+d
        a = b
        b = c
        c = d
        d = temp
    return a'''
'''
def odd_squares(n):
    for i in range(1, n * 2):
        if i % 2 != 0:
            print(i ** 2)
odd_squares(15)
'''
# teacher example
'''
def odd_squares(n)
count = 0
x = 1
while count < n:
    if (x**0.5) == int(x**0.5):
        print(x)
        count+=1
    x+=2
odd_squares(15)
'''

def pattern1(h):
    for x in range(h):
        for y in range(h):
            if max(x, y) % 2 == 0:
                print("--",end = "")
            else:
                print("##", end = "")
        print()

pattern1(5)

def pattern2(h):
    for y in range(h):
        for x in range(h):
            if x % 2 == 0 and y % 2 == 0:
                print("+", end = "")
            elif x % 2 == 0:
                print("|", end = "")
            elif y % 2 == 0:
                print("-", end = "")
            else:
                print("?", end = "")
        print()

pattern2(7)














