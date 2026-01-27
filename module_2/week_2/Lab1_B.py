# Write a program named Lab1_B.py that will calculate the sales tax on a purchased item.

# All outputs should be rounded to two decimal places.	

# Input:
# Enter the price of the item: 
# Enter the sales tax percentage: 

# Output:
# Your total is ${price}

# You may assume:
# All inputs are valid numbers greater than or equal to 0
# Sales tax is entered as a percentage

item_price = float(input("Enter the price of the item: "))
sales_tax = 0.01 * float(input("Enter the sales tax percentage: "))

total_price = item_price + (item_price * sales_tax)
print(f"Your total is ${total_price:.2f}")

