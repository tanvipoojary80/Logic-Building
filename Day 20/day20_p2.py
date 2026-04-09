# Pattern 2
#     1
#   1 2 1
# 1 2 3 2 1

n = 3
for i in range(1, n + 1):
    print(" " * (n - i), end="") # spaces
    # increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    # decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()


# output:
#     1
#   1 2 1
# 1 2 3 2 1