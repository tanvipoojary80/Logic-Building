# Check Whether a Number is Prime or Not:
# Write a program that checks if a number entered by the user is a prime number. For example:
# Input: Enter a number: 17
# Output: 17 is a prime number.

num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
        
# output:
# Enter a number: 29
# 29 is a prime number.
