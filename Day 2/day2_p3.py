# Program to Check Whether the Number is a Multiple of 7:
# Write a program that verifies if a number entered by the user is a multiple of 7. For example:
# Input: Enter a number: 14
# Output: 14 is a multiple of 7

num = int(input("Enter a number: ")) # Taking input from user
if num % 7 == 0: # Checking multiple of 7
    print(num, "is a multiple of 7")
else:
    print(num, "is not a multiple of 7")

# output 1:
# Enter a number: 35
# 35 is a multiple of 7

#output 2:
# Enter a number: 87
# 87 is not a multiple of 7