#
n = int(input("Enter an integer value n to calculate n!: "))
factorial = 1
i = 0
while i != n:
    i+=1
    factorial*=i

print(f"{n}! = {factorial}")

'''
n = int(input("Enter an integer value n to calculate n!: "))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i

print(f"{n}! = {factorial}")
'''