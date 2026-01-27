# Create a Python program that calculates the distances between points on a coordinate plane
import math
x1 = float(input("Enter the 1st x value: "))
y1 = float(input("Enter the 1st y value: "))
x2 = float(input("Enter the 2nd x value: "))
y2 = float(input("Enter the 2nd y value: "))

d = (math.sqrt((math.pow(x2-x1),2) + (math.pow(y2-y1),2)))

