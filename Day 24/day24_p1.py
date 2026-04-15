'''Find the Second Largest Element in an Array
Find the second largest element in the array.
Input: [10, 20, 4, 45, 99]
Output: Second Largest: 45'''


arr = list(map(int, input("Enter elements: ").split()))
largest = second = float('-inf')
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second Largest:", second)

'''output:
Enter elements: 23 76 98 45 70
Second Largest: 76'''