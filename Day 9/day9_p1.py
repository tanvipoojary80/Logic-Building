# Pattern 1
# 1             1
# 1 2         2 1
# 1 2 3     3 2 1
# 1 2 3 4 4 3 2 1

n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):  # Left increasing numbers
        print(j, end=" ")
    for j in range(2 * (n - i)):  # Spaces
        print(" ", end=" ")
    for j in range(i, 0, -1): # Right decreasing numbers
        print(j, end=" ")
    print()

# output:
# 1             1 
# 1 2         2 1 
# 1 2 3     3 2 1 
# 1 2 3 4 4 3 2 1 