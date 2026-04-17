'''Longest Word in a Sentence
Find the longest word in a given sentence.
Input: "The quick brown fox"
Output: "quick"'''

sentence = "The quick brown fox"
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)

'''output:
Longest word: quick'''