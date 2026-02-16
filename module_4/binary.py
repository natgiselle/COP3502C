# Write a python program that takes a number n as input and prints as alternating binary pattern with n rows and 5 columns
# example for height: 5
'''
10101
01010
10101
01010
10101
'''

n = int(input("Enter an integer n (number of rows): "))

for i in range(1, n+1):
    for j in range(1, n + 1):
        if i % 2 == 0:
            if j % 2 == 0:
                print('1', end ='')
            else:
                print('0', end ='')
        else:
            if j % 2 == 0:
                print('0', end='')
            else:
                print('1', end='')
    print()