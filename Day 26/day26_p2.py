'''Find the First Non-Repeating Character
Identify the first character that does not repeat in the string.
Input: "swiss"
Output: "w"
'''

s = "swiss"
for char in s:
    if s.count(char) == 1:
        print("First non-repeating character:", char)
        break
    
'''output:
First non-repeating character: w'''