# Write a program where the user enters three numbers, and the program finds and displays the largest number among them.
# Example:
# Input: Enter three numbers: 12, 25, 7
# Output: The largest number is: 25

nums = input("Enter three numbers: ")
a, b, c = map(int, nums.split(","))
if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)
    

# output:
# Enter three numbers: 90,20,87
# The largest number is: 90

