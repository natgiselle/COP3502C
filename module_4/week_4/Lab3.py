import math
result = 0.0
menu_selection = 1
calculation = 0
sum_of_calculations = 0
show_menu = True
while menu_selection != 0:
    if show_menu == True:
        if menu_selection >=1 and menu_selection <= 6:
            print(f"Current Result: {round(result, 2)}")
        print("\nCalculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")
    menu_selection = int(input("\nEnter Menu Selection: "))
    if menu_selection == 0:
        print("Thanks for using this calculator. Goodbye!")
        break
    if menu_selection >=1 and menu_selection <= 6:
        operand1 = (input("Enter first operand: "))
        operand2 = (input("Enter second operand: "))
        num1 = result if operand1 == "RESULT" else float(operand1)
        num2 = result if operand2 == "RESULT" else float(operand2)
        if menu_selection == 1:
            show_menu = True
            result = num1 + num2
            calculation += 1
            sum_of_calculations += result

        elif menu_selection == 2:
            show_menu = True
            result = num1 - num2
            calculation += 1
            sum_of_calculations += result

        elif menu_selection == 3:
            show_menu = True
            result = num1 * num2
            calculation += 1
            sum_of_calculations += result

        elif menu_selection == 4:
            show_menu = True
            result = num1 / num2
            calculation += 1
            sum_of_calculations += result

        elif menu_selection == 5:
            show_menu = True
            result = num1 ** num2
            calculation += 1
            sum_of_calculations += result

        elif menu_selection == 6:
            show_menu = True
            result = math.log(num2, num1) # swapped 
            calculation += 1

            sum_of_calculations += result
    elif menu_selection == 7:
        if calculation == 0:
            show_menu = False
            print("Error: No calculations yet to average!")
            continue
        else:
            print(f"Sum of calculations: {round(sum_of_calculations, 2)}")
            print(f"Number of calculations: {calculation}")
            print(f"Average of calculations: {round(sum_of_calculations/calculation, 2)}")
            show_menu = False
    else:
        print("Error: Invalid selection!")
        show_menu = False
        continue