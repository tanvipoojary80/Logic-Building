# Program to Perform Swapping of Two Numbers:
# Write a program to swap two numbers entered by the user. For example:
# Input: Enter first number: 10, Enter second number: 20
# Output:
# Before swapping: a = 10, b = 20
# After swapping: a = 20, b = 10

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: a =", a, ", b =", b)
temp = a # Swapping using temp variable
a = b
b = temp
print("After swapping: a =", a, ", b =", b)

# output:
# Enter first number: 2
# Enter second number: 5
# Before swapping: a = 2 , b = 5
# After swapping: a = 5 , b = 2
