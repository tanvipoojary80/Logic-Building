# Pattern 3
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0

n = 4
for i in range(n):
    for j in range(n):
        print((i + j) % 2, end=" ")
    print()
    
# output:
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0
