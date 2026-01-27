# Compound Interest Calculator
# Write a program called compound_interest.py that calculates compound interest based on the following user inputs:
# initial principle
# interest rate
# number of times per year that interest is applied
# number of years elapsed
import math
p = float(input("Initial principle: "))
r = float(input("Interest rate: "))
n = float(input("How many times does interest apply annually: "))
t = float(input("How many years have passed: "))
a = p * math.pow(1 + (r * 0.01)/n,n*t)
print(f"You now have ${a:.2f}")

