# Pattern 2:
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 4 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

n = 4
size = 2 * n - 1  # total rows/columns
for i in range(size):
    for j in range(size):
        
        # find minimum distance from all 4 sides
        val = n - min(i, j, size - 1 - i, size - 1 - j)
        print(val, end=" ")
    print()

# output:
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 4 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4