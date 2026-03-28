# DAY 10
# Pattern 1
# A
# B B
# C C C
# D D D D
# E E E E E

n = 5
for i in range(n):
    ch = chr(65 + i)   # Convert number to uppercase letter (A=65)
    for j in range(i + 1):
        print(ch, end=" ")
    print()

# output:
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 


