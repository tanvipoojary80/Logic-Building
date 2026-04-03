# Print Factorial Series:
# Write a program that prints the factorial of numbers from 1 to N, where the user enters N. For example:
# Input: Enter a number: 5
# Output:
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    print(f"{i}! = {fact}")

# output:
# Enter a number: 6
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720
