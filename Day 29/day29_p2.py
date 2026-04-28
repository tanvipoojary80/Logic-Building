'''Search an Element in a Matrix
Search for a given element in a matrix and return its position.
Input:
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], Target = 5
Output:
Position: (1, 1) (0-based index)
'''

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
A = []
print("Enter rows :")
for i in range(rows):
    A.append(list(map(int, input().split())))
target = int(input("Enter element to search: "))
found = False
for i in range(rows):
    for j in range(cols):
        if A[i][j] == target:
            print("Position:", (i, j))
            found = True
if not found:
    print("Element not found")
    
'''output:
Enter number of rows: 3
Enter number of columns: 3
Enter rows :
2 4 3
1 2 4
5 6 1
Enter element to search: 3
Position: (0, 2)'''