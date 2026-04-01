# Write a Program to Calculate the Power of a Number:
# Write a program that takes a base and an exponent as input and calculates the power of the base raised to the exponent using both manual calculation and the pow() function. For example:
# Input: Base: 2, Exponent: 3
# Output:
# Result using manual calculation: 8
# Result using pow(): 8

# Input from user
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
# Manual calculation
result_manual = 1
for i in range(exponent):
    result_manual *= base
# Using pow() function
result_pow = pow(base, exponent)
print("Result using manual calculation:", result_manual)
print("Result using pow():", result_pow)

# output:
# Enter base: 5
# Enter exponent: 2
# Result using manual calculation: 25
# Result using pow(): 25