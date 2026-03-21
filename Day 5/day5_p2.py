# Write a Program to Check Whether a Character is a Vowel or Consonant:
# Write a program to check whether a character entered by the user is a vowel (a, e, i, o, u) or a consonant. For example:
# Input: Enter a character: e
# Output: e is a vowel.

ch = input("Enter a character: ")
if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(ch, "is a vowel.")
else:
    print(ch, "is a consonant.")


# output:
# Enter a character: i
# i is a vowel.