# calculator.py

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Error: Invalid operator"

def main():
    print("Welcome to the Python Calculator!")

    try:
        # Get user input
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        # Perform calculation
        result = calculate(number1, number2, operator)

        # Display result
        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
