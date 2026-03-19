# Print the Multiplication Table of a Given Number:
# Write a program where the user enters a number, and the program prints its multiplication table. For example:
# Input: Enter a number: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 10 = 50

num = int(input("Enter a number: ")) #  Take input from user
for i in range(1, 11): #  Loop from 1 to 10
    print(f"{num} x {i} = {num * i}") #  Print multiplication table

# output:
# Enter a number: 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20
