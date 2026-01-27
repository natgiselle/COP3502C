# First program; Module 2 discussion
'''
Multi-line 
Comment
With
3
Single
Quotes
'''

print("Hello world! :3")

a = 5
b = 6
c = a + b

print("The sum of ", a, " and ", b, " is ", c,".", sep="")
# sep is a keyword arguement which print whatver is in the str

num_one = int(input("Enter 1st number: "))
num_two = int(input("Enter 2nd number: "))

num_three = num_one % num_two
print("The answer is " + str(num_three))