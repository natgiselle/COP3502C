'''
# What is the output of each print statement?

a = [1, 2, [3, 'John', 4], 'Hi']

print(a[2][-1])     
print()
print(a[-1][-1])
print()
print(a[0:-3])      
print()
print(a[3:0:-2])
'''

'''
b = [9, 7, 11, 10, 8, 1]
c = [item - 1 for item in b if item % 2 == 1]
c[1:-1] = 'hi'
print(c)
'''

'''
a = [1] + [2]
a.extend([4, 5])
a.append(3)

print(a[3:])
'''

'''
a = [1, 2, 4] + [2, 1, 5]
a.extend([4, 5, 3, 2, 1])
b = set(a)
print(b)
'''

fruits = {'a': 'apple', 'b': 'banana', 'c': 'cranberry'}
fruits['d'] = 'dragon fruit'

print(fruits['c'])


print('banana' in fruits)        


print(len(fruits))               


print('d' in fruits)             