'''Find Duplicate Characters in a String
Identify all characters that appear more than once in a string.
Input: "programming"
Output: ["r", "g", "m"]
'''

text = input("Enter a string: ")
duplicates = []
for ch in text:
    if text.count(ch) > 1 and ch not in duplicates:
        duplicates.append(ch)
print("Duplicate characters:", duplicates)

'''output:
Enter a string: hello
Duplicate characters: ['l'] '''