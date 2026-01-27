# Write a program named Lab1_A.py that will convert a temperature from Celsius to Fahrenheit.
# All outputs should be rounded to one decimal place.	

# Input:
# Enter the temperature in Celsius: 

#Output:
# That is {temperature} degrees Fahrenheit!

# You may assume:
# All inputs are valid numbers

degrees_in_celsius = float(input("Enter the temperature in Celsius: "))
celsius_to_fahrenheit = ((degrees_in_celsius * (9/5)) + 32)

print(f"That is {celsius_to_fahrenheit:.1f} degrees Fahrenheit!")