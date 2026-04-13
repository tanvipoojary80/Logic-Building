# Finding the Longest Sequence of Consecutive 1s in a Binary Array
# Write a program to find the longest sequence of consecutive 1s in a binary array.
# Input: binaryArray = [1, 1, 0, 1, 1, 1]
# Output: 3

arr = list(map(int, input("Enter binary array : ").split()))
max_count = 0
count = 0
for num in arr:
    if num == 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print("Output:", max_count)

# output:
# Enter binary array : 1 1 1 0 1 1 1
# Output: 3