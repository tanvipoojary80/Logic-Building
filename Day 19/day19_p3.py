# Pattern 3:
# E
# D E
# C D E
# B C D E
# A B C D E

n = 5
for i in range(n):
    start = ord('E') - i  # starting character
    for j in range(start, ord('E') + 1):
        print(chr(j), end=" ")
    print()
    
# ooutput:
# E
# D E
# C D E
# B C D E
# A B C D E
