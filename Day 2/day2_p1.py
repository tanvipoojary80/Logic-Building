# Program to Check Whether the Number is Odd or Even:
# Write a program that checks whether a number entered by the user is odd or even. For example:
# Input: Enter a number: 7
# Output: 7 is an odd number

num = int(input("Enter a number: ")) # Taking input from user
if num % 2 == 0: # Checking odd or even
    print(num, "is an even number")
else:
    print(num, "is an odd number")

# output 1:
# Enter a number: 23
# 23 is an odd number

# output 2:
# Enter a number: 22
# 22 is an even number