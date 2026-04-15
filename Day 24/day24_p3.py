'''Move Zeros to the End of an Array
Move all zeros in the array to the end while maintaining the relative order of non-zero elements.
Input: [0, 1, 2, 0, 3, 4, 0]
Output: [1, 2, 3, 4, 0, 0, 0]
'''

arr = list(map(int, input("Enter elements: ").split()))
non_zero = [x for x in arr if x != 0]
zeros = [0] * arr.count(0)
result = non_zero + zeros
print("Updated array:", result)

'''output
Enter elements: 0 1 2 0 3 4 0
Updated array: [1, 2, 3, 4, 0, 0, 0]'''