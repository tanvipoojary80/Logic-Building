'''Matrix Multiplication
Multiply two matrices if the number of columns in the first matrix equals the number of rows in the second.
Input:
A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]
Output:
[[19, 22], [43, 50]]

'''


r1 = int(input("Rows of A: "))
c1 = int(input("Columns of A: "))
A = []
print("Enter rows of A :")
for i in range(r1):
    A.append(list(map(int, input().split())))
r2 = int(input("Rows of B: "))
c2 = int(input("Columns of B: "))
B = []
print("Enter rows of B :")
for i in range(r2):
    B.append(list(map(int, input().split())))
if c1 != r2:
    print("Not possible")
else:
    result = [[0]*c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]
    print("Result:")
    for row in result:
        print(row)
        
'''output:
Rows of A: 2
Columns of A: 2
Enter rows of A :
2 4
5 4
Rows of B: 2
Columns of B: 2
Enter rows of B :
5 6 
4 8
Result:
[26, 44]
[41, 62]'''