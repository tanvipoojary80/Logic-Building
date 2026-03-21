# Calculate the Sum of Digits of a Given Number:
# Write a program that calculates the sum of the digits of a number entered by the user. For example:
# Input: Enter a number: 1234
# Output: Sum of digits: 10

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10   # get last digit
    sum += digit       # add to sum
    num = num // 10    # remove last digit
print("Sum of digits:", sum)

# output:
# Enter a number: 5461
# Sum of digits: 16