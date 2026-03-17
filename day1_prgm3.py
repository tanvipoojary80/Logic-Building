#Program to Find the Larger Number Among Two Numbers:
#Write a program to compare two integers entered by the user and print the larger one. For example:
#Input: Enter two numbers: 15, 20
#Output: The larger number is: 20

# Take two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Compare numbers
if num1 > num2:
    print("The larger number is:", num1)
elif num2 > num1:
    print("The larger number is:", num2)
else:
    print("Both numbers are equal")
