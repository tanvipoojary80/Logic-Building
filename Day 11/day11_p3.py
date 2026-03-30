# Write a program where the user enters a number N, and the program calculates the sum of all natural numbers up to N. For example:
# Input: Enter a number: 5
# Output: The sum of the first 5 natural numbers is 15.

n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("The sum of the first", n, "natural numbers is", total)

# output:
# Enter a number: 8
# The sum of the first 8 natural numbers is 36
