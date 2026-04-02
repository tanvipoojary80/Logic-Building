'''Write a Program to Display All Factors of a Number:
Write a program to find and print all factors of a number entered by the user. For example:
Input: Enter a number: 28
Output: Factors of 28: 1, 2, 4, 7, 14, 28
'''

n = int(input("Enter a number: "))
print("Factors of", n, "are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=", ")
        
''' output:
Factors of 86 are:
1, 2, 43, 86'''