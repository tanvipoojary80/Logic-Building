# Print Prime Numbers Within a Range:
# Write a program to display all prime numbers between two intervals entered by the user. For example:
# Input: Enter two numbers: 10, 30
# Output: Prime numbers between 10 and 30: 11, 13, 17, 19, 23, 29

nums = input("Enter two numbers: ")
start, end = map(int, nums.split(","))
print("Prime numbers between", start, "and", end, end=": ")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=", ")
            
# output 1:
# Enter two numbers: 10,30
# Prime numbers between 10 and 30: 11, 13, 17, 19, 23, 29,

# output 2:
# Enter two numbers: 20,40
# Prime numbers between 20 and 40: 23, 29, 31, 37, 