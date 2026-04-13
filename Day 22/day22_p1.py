# Print the Array in Sorted Order (Ascending and Descending):
# Write a program to sort an array in ascending and descending order. For example:
# Input: [5, 3, 8, 1]
# Output:
# Ascending: [1, 3, 5, 8]
# Descending: [8, 5, 3, 1]

arr = [5, 3, 8, 1]
# Ascending order
arr.sort()
print("Ascending:", arr)
# Descending order
print("Descending:", arr[::-1])

# OUTPUT:
# Ascending: [1, 3, 5, 8]
# Descending: [8, 5, 3, 1]