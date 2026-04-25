# Check Anagrams
# Determine if two strings are anagrams of each other.
# Input: "listen", "silent"
# Output: "Anagrams"

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")

# OUTPUT 1:
# Enter first string: listen
# Enter second string: silent
# Anagrams

# OUTPUT 2:
# Enter first string: Hello
# Enter second string: world
# Not Anagrams