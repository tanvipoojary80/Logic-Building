# Finding the Most Frequent Element in an Array
# Write a program to find the most frequent element in an array.
# Input: array = [1, 2, 2, 3, 3, 3]
# Output: 3

arr = list(map(int, input("Enter array : ").split()))
max_count = 0
most_frequent = arr[0]
for i in arr:
    count = arr.count(i)
    if count > max_count:
        max_count = count
        most_frequent = i
print("Output:", most_frequent)

# output:
# 5 6 6 7 7