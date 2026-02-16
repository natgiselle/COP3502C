unit_from = input("Enter the unit you are converting from: ")
unit_to = input("Enter the unit you are converting to: ")
temperature = float(input(f"Enter the temperature in {unit_from}: "))

if unit_from == "Fahrenheit":
    if unit_to == "Celsius":
        degrees_celsius = (5/9) * (temperature - 32)
        print(f"That is {degrees_celsius:.1f} degrees {unit_to}.")
    elif unit_to == "Kelvin":
        degrees_kelvin = (5/9) * (temperature - 32) + 273.15
        print(f"That is {degrees_kelvin:.1f} degrees {unit_to}.")
    elif unit_to == unit_from:
        print(f"That is {temperature:.1f} degrees {unit_to}.")


if unit_from == "Celsius":
    if unit_to == "Fahrenheit":
        degrees_fahrenheit = (temperature * (9/5)) + 32
        print(f"That is {degrees_fahrenheit:.1f} degrees {unit_to}.")
    if unit_to == "Kelvin":
        degrees_kelvin = temperature + 273.15
        print(f"That is {degrees_kelvin:.1f} degrees {unit_to}.")
    elif unit_to == unit_from:
        print(f"That is {temperature:.1f} degrees {unit_to}.")

if unit_from == "Kelvin":
    if unit_to == "Fahrenheit":
        degrees_fahrenheit = (temperature - 273.15) * (9/5) + 32
        print(f"That is {degrees_fahrenheit:.1f} degrees {unit_to}.")
    elif unit_to == "Celsius":
        degrees_celsius = temperature - 273.15
        print(f"That is {degrees_celsius:.1f} degrees {unit_to}.")
    elif unit_to == unit_from:
        print(f"That is {temperature:.1f} degrees {unit_to}.")