# first makes 4 elements of the value inside times 4 so it would be a list of 4 lists of 4 elements of zero
x = [[0] * 4] * 4
x[0][1] = 9
print(x)

# creates seperate objects in every list run one by one through a for loop
x = [[0] * 4 for _ in range(4)]
x[0][1] = 9
print(x)
