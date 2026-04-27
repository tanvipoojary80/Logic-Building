''' Matrix Addition
Add two matrices of the same dimensions.
Input: 
A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]
Output:
[[6, 8], [10, 12]]
'''

rows = int(input("Rows: "))
cols = int(input("Cols: "))
print("Matrix A:")
A = [list(map(int, input().split())) for _ in range(rows)]
print("Matrix B:")
B = [list(map(int, input().split())) for _ in range(rows)]
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    result.append(row)
print(result)

''' output:
Rows: 2
Cols: 2
Matrix A:
2 3
6 4
Matrix B:
9 5 
4 9
[[11, 8], [10, 13]] '''