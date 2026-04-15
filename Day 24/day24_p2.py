'''Remove Duplicates from an Array
Remove all duplicates from the given array and return the unique elements..
Input: [1, 2, 2, 3, 4, 1, 5]
Output: [1, 2, 3, 4, 5]
'''

arr = list(map(int, input("Enter elements: ").split()))
unique = list(set(arr)) # Remove duplicates
print("Array without duplicates:", unique)

'''output:
Enter elements: 1 1 2 3 3 3 4 5
Array without duplicates: [1, 2, 3, 4, 5]'''