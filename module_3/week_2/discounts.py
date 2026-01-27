'''
Write a program called discounts.py that will calculate the final price of an item after applying several discounts. 
The discounts will apply multiplicatively to each other.
The user will enter input in the following order:
Price of the item
Is it black friday
Do you have a coupon
Do you have an employee discount

The available discounts are:
black friday (40% off), coupon (5% off), employee discount (20% off)
The output will always display exactly two decimal places.
'''

price = float(input("Enter the price: "))

black_friday = input("Is it black friday [y/n]: ")
if black_friday == "y":
   price *= 0.60
elif black_friday == "n":
    price = price

coupon = input("Do you have a coupon [y/n]: ")
if coupon == "y":
    price *= 0.95
elif coupon == "n":
    price = price

employee = input("Do you have an employee discount [y/n]: ")
if employee == "y":
    price *= 0.80
elif employee == "n":
    price = price

print(f"The final price is: ${price:.2f}")