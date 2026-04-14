# Reverse an Array
# Reverse the order of elements in the given array.
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

arr = list(map(int, input("Enter numbers: ").split()))
rev = arr[::-1]
print("Reversed Array:", rev)

# OUTPUT:
# Enter numbers:  6 7 8 9
# Reversed Array: [9, 8, 7, 6]
