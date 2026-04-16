'''Find the Frequency of Each Element in an Array
Calculate the frequency of each element in the array.
Input: [1, 2, 2, 3, 1, 4, 5, 1]
Output: {1: 3, 2: 2, 3: 1, 4: 1, 5: 1}'''

arr = list(map(int, input("Enter elements: ").split()))
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)

'''output:
Enter elements: 2 3 2 4 3 2
{2: 3, 3: 2, 4: 1}'''