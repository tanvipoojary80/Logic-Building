# Perfect Number Write a program to determine if a number is a perfect number.
# Input: number = 6
# Output: Perfect Number
# Explanation: 6 is a perfect number because its divisors (1, 2, 3) sum up to 6.

# Function to check perfect number
num = int(input("Enter a number: "))
sum_div = 0
# Find divisors
for i in range(1, num):
    if num % i == 0:
        sum_div += i
# Check condition
if sum_div == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
    
# output 1:
# Enter a number: 28
# Perfect Number

# output:
# Enter a number: 10
# Not a Perfect Number