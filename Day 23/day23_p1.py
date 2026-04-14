# Find the Missing Number in an Array
# Given an array of numbers from 1 to n with one number missing, find the missing number.
# Input: [1, 2, 4, 5, 6]
# Output: Missing Number: 3

arr = list(map(int, input("Enter numbers: ").split()))
n = len(arr) + 1
for i in range(1, n + 1):
    if i not in arr:
        print("Missing Number:", i)
        break

# output:
# Enter numbers: 1 3 4 5
# Missing Number: 2