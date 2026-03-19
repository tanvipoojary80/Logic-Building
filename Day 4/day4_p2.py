# Write a Program to Make a Simple Calculator Using a Switch Case:
# Write a program that acts as a calculator, taking two numbers and an operator (+, -, *, /) from the user, and performing the operation based on the operator. For example:
# Input: Enter first number: 10, Operator: +, Second number: 20
# Output: 10 + 20 = 30


num1 = float(input("Enter first number: ")) #  Take input from user
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
# Perform operation using match-case (switch case)
match operator:
    case '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    case '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    case '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    case '/':
        #  Check division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed")
    case _:
        #  Invalid operator
        print("Invalid operator")


# output 1:
# Enter first number: 50
# Enter operator (+, -, *, /): +
# Enter second number: 30
# 50.0 + 30.0 = 80.0

# output 2:
# Enter first number: 50
# Enter operator (+, -, *, /): -
# Enter second number: 30
# 50.0 - 30.0 = 20.0

# Enter first number: 25
# Enter operator (+, -, *, /): *
# Enter second number: 5
# 25.0 * 5.0 = 125.0

# Enter first number: 40
# Enter operator (+, -, *, /): /
# Enter second number: 5
# 40.0 / 5.0 = 8.0