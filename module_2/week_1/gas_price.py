# Gas Price Calculator
# Write a program called gas_price.py that calculates how much refueling a car will cost. The user will enter:
# The car’s tank capacity
# How full the car is currently
# The price of gas

car_tank_capacity = float(input("How big is your car's gas tank: "))
current_gallons = float(input("How many gallons are in your tank now: "))
price_per_gallon = float(input("What is the price of gas per gallon: "))
gas_price = (car_tank_capacity - current_gallons) * price_per_gallon
print(f"Your gas will cost ${gas_price:.2f}")
