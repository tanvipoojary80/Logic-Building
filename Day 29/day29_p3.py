'''Matrix Transpose
Find the transpose of a matrix (convert rows to columns and vice versa).
Input:
A = [[1, 2, 3], [4, 5, 6]]
Output:
[[1, 4], [2, 5], [3, 6]]
'''

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
A = []
print("Enter rows :")
for i in range(rows):
    A.append(list(map(int, input().split())))
transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(A[i][j])
    transpose.append(row)
print("Transpose matrix:")
for row in transpose:
    print(row)
    
'''output:
Enter rows :
3 4 2
3 4 1
6 7 5
Transpose matrix:
[3, 3, 6]
[4, 4, 7]
[2, 1, 5]
'''