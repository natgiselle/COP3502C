# creation of tuples

# TUPLES CAN BE INITALIZED WITHOUT PARENTHESES
colors = ("red", "green", "yellow")
print(f"Type of {type(colors)}")

# Tples are IMMUTABLE 
# cannot change, add, remove, or change any elements once created
single = (42,)

mix = (1,2,3)

# mixing tuples

mix = ("hey", 3, 3,1415926)

# accessing tuples
print(mix[0])

# unpacking tuples
nums = (3,4)
x,y = nums

# converting tuples
t = ("h", "e", "l", "l", "o")
