def calculator():
    print("Welcome to the Anveshi's calculator!")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("What you wanna do :")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1-4): ")
    if choice == '1':
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of subtracting {num2} from {num1} is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of multiplying {num1} and {num2} is: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of dividing {num1} by {num2} is: {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input!")
calculator()