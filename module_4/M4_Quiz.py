'''
What is the output of the following program?
sum = 0
for i in range(1, 4):
    for j in range(i + 2, 5):
        sum += i * j
print(sum)

What is the output of the following program?


var = 7

while True:
    var += 3
    if var == 10:
        print(var, end="")
        break

print(var)


What is the output of the following program?

x = 55

for i in range(3, 6, -1):
    x += i
    print(x, end="")

print(x)
'''

#What is the output of the following code?

x = 3

while x < 15:
    if x % 2 == 0:
        x = x + 1
    elif x % 2 == 1:
        x = x + 3
    if x % 5 == 0:
        break

print(x)