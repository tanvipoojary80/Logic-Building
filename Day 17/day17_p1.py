# Write a Program to Convert Binary Numbers to Decimal and Vice Versa Manually:
# Write a program that uses user-defined functions to convert binary numbers to decimal and decimal numbers to binary. For example:
# Input: Enter a binary number: 1010
# Output: Decimal equivalent: 10
# Input: Enter a decimal number: 10
# Output: Binary equivalent: 1010


# Binary to Decimal
def binary_to_decimal(b):
    decimal = 0
    power = 0
    while b > 0:
        digit = b % 10
        decimal += digit * (2 ** power)
        b //= 10
        power += 1
    return decimal
# Decimal to Binary
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary
# Input & Output
b = int(input("Enter a binary number: "))
print("Decimal equivalent:", binary_to_decimal(b))
d = int(input("Enter a decimal number: "))
print("Binary equivalent:", decimal_to_binary(d))

# output:
# Enter a binary number: 1101
# Decimal equivalent: 13
# Enter a decimal number: 13
# Binary equivalent: 1101
