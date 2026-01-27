# Change Calculator
# Write a program called change.py that calculates how much change a customer is owed. The program user will enter the following:
# Item price
# How much the customer paid
# You may assume that the customer paid more than they owed
# The program will also need to account for 6% sales tax.

item_price = float(input("What is the listed price of the item: "))
customer_payment = float(input("How much did the customer pay: "))
change = customer_payment - (item_price * 0.06 + item_price)
print(f"They get ${change:.2f} in change")


