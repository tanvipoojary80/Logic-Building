# Program to Check Whether the Number is Divisible by 5:
# Write a program that determines if a number entered by the user is divisible by 5. For example:
# Input: Enter a number: 25
# Output: 25 is divisible by 5.

num = int(input("Enter a number: ")) # Taking input from user
if num % 5 == 0: # Checking divisibility by 5
    print(num, "is divisible by 5")
else:
    print(num, "is not divisible by 5")
 
 # output 1:
 # Enter a number: 25
 # 25 is divisible by 5

# output 2:
# Enter a number: 49
# 49 is not divisible by 5