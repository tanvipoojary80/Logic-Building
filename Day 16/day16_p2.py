# Check if an Integer Can Be Expressed as the Sum of Two Prime Numbers:
# Write a program to check if a number can be expressed as the sum of two prime numbers. Print all such combinations. For example:
# Input: Enter a number: 34
# Output:
# 34 = 3 + 31
# 34 = 5 + 29
# 34 = 11 + 23
# 34 = 17 + 17

n = int(input("Enter a number: "))
for i in range(2, n):
    count1 = 0
    for j in range(2, i):
        if i % j == 0:
            count1 += 1
    count2 = 0
    for j in range(2, n - i):
        if (n - i) % j == 0:
            count2 += 1
    if count1 == 0 and count2 == 0:
        print(n, "=", i, "+", n - i)
        
# output:
# Enter a number: 24
# 24 = 5 + 19
# 24 = 7 + 17
# 24 = 11 + 13
# 24 = 13 + 11
# 24 = 17 + 7
# 24 = 19 + 5
# 24 = 23 + 1


