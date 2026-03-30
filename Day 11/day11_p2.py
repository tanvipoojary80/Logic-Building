# Write a program to determine whether a given year is a leap year. For example:
# Input: Enter a year: 2024
# Output: 2024 is a leap year.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# output:
# Enter a year: 2004
# 2004 is a leap year.
