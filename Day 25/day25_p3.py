'''Count Words in a String
Count the number of words in a sentence.
Input: "I love programming"
Output: 3
'''

text = input("Enter a sentence: ")
words = text.split()   # splits sentence into words
count = len(words)
print(count)

'''otuput:
Enter a sentence: hello world
2'''