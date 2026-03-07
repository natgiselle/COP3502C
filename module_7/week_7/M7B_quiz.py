'''
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

x = my_dict['banana']
y = my_dict.get('grape', 5)
z = len(my_dict)
print(x+y+z)
'''

'''
x = {2,3,4,5}
y = {3,4,5,8}
z= x.union(y)
print(z[1:3])
'''

data = {'letters': ['a', 'b', 'c'],
        'numbers': (1, 2, 3),
        'colors': {'primary': 'red', 'secondary': 'blue'}}

result = data['letters'][1] + str(data['numbers'][2]) + data['colors']['primary'][0]

print(result)