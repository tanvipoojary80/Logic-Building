'''Find All Substrings of a String
Print all possible substrings of a string.
Input: "abc"
Output: ["a", "b", "c", "ab", "bc", "abc"]
'''

s = "abc"
substrings = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.append(s[i:j])
print(substrings)

'''output:
['a', 'ab', 'abc', 'b', 'bc', 'c']'''