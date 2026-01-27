# Write a program named Lab1_C.py that will calculate the number of days between 2 dates.

# Input:
# Enter the year for date 1: 
# Enter the month for date 1: 
# Enter the day for date 1: 
# Enter the year for date 2: 
# Enter the month for date 2: 
# Enter the day for date 2: 

# Output:
# The difference between {month1}/{day1}/{year1} and {month2}/{day2}/{year2} is {difference} days!

# You may assume:
# All inputs are valid integers greater than 0
# Years always have exactly 12 months
# Months always have exactly 30 days

year_1 = int(input("Enter the year for date 1: "))
month_1 = int(input("Enter the month for date 1: "))
day_1 = int(input("Enter the day for date 1: "))
year_2 = int(input("Enter the year for date 2: "))
month_2 = int(input("Enter the month for date 2: "))
day_2 = int(input("Enter the day for date 2: "))

difference_in_days = ((year_2 - year_1) * 360) + ((month_2 - month_1) * 30) + ((day_2 - day_1))

print(f"The difference between {month_1}/{day_1}/{year_1} and {month_2}/{day_2}/{year_2} is {abs(difference_in_days)} days!")