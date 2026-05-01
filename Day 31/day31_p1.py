'''Factorial of a Number
Task: Define a recursive function factorial(n) that returns the product of all positive integers from 1 up to n.
Input: n = 5
Expected Output: 120
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter a number: "))
print("Factorial:", factorial(n))

'''output:
Enter a number: 6
Factorial: 720'''