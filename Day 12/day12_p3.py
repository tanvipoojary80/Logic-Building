# Write a Program to Find the GCD or HCF of Two Numbers:
# Write a program where the user enters two numbers, and the program calculates their greatest common divisor (GCD) or highest common factor (HCF). For example:
# Input: Enter two numbers: 60, 48
# Output: The GCD of 60 and 48 is 12.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("The GCD of", a, "and", b, "is", gcd)

# output:
# Enter first number: 40
# Enter second number: 80
# The GCD of 40 and 80 is 40
