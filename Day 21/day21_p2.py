# Largest Prime Factor Write a program to find the largest prime factor of a given number.
# Input: number = 28
# Output: 7

num = int(input("Enter a number: "))
i = 2
largest = 0
while i <= num:
    if num % i == 0:
        largest = i
        num = num // i   # divide the number
    else:
        i += 1
print("Largest Prime Factor:", largest)

# output:
# Enter a number: 25
# Largest Prime Factor: 5
