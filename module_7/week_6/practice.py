
# Shallow Copy
a = [[5], 6]
b = a[:]
a[0][0] = 10 # first element of a is a sublist when you update that 10 it impacts b also
print(a,b)


# Deep Copy
import copy 
a = [[5], 6]
b = copy.deepcopy(a)
a[0][0] = 10
print(a,b)
