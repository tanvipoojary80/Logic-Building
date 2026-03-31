# Print Fibonacci Series:
# Write a program to print the Fibonacci series up to a number N entered by the user. For example:
# Input: Enter the number of terms: 7
# Output: Fibonacci series: 0 1 1 2 3 5 8

n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# output:
# Enter the number of terms: 8
# Fibonacci series:
# 0 1 1 2 3 5 8 13