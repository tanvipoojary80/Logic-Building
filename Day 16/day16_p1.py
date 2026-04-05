# Write a Program to Check Whether a Number is a Palindrome:
# Write a program to determine if a number is a palindrome. For example:
# Input: Enter a number: 121
# Output: 121 is a palindrome.

num = int(input("Enter a number: "))
original = num
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
if original == reversed_num:
    print(original, "is a palindrome.")
else:
    print(original, "is not a palindrome.")

# output:
# Enter a number: 131
# 131 is a palindrome.
