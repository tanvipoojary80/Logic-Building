# Write a Program to Find the LCM of Two Numbers:
# Write a program where the user enters two numbers, and the program calculates their least common multiple (LCM). For example:
# Input: Enter two numbers: 4, 6
# Output: The LCM of 4 and 6 is 12.

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Find the greater number
max_num = max(num1, num2)
# Loop to find LCM
while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        lcm = max_num
        break
    max_num += 1
print("The LCM of", num1, "and", num2, "is", lcm)

# output:
# Enter first number: 9
# Enter second number: 4
# The LCM of 9 and 4 is 36