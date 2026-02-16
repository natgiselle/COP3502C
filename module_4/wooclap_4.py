# Create an increasing pattern that alternates between * and #
# inpt : # of rows
# odd rows use * 

# rows = int(input("Enter rows: "))

# take example numbers

'''
sample output for 5 rows: 
*
##
***
####
*****


for last line do pattern * i
when i is 1, with row input of 5
i in range 5 i starts with zero
zero mod 2 equals zero so for the first row it is printing #

rows, rows + 1
or can do i + 1
'''

size = int(input("Enter size (3-9): "))
for i in range(size):
    for j in range(size):
        if i == 0 or i == size:
            print("*", end = "")
        elif j == 0:
            print("*", end = "")
        else:
            print(" ", end = "")
print()