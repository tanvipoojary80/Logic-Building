''' Count Vowels and Consonants
Count the number of vowels and consonants in a string.
Input: "hello"
Output: Vowels: 2, Consonants: 3
'''

text = input("Enter a string: ").lower()
vowels = "aeiou"
v_count = 0
c_count = 0
for ch in text:
    if ch.isalpha():   # check only letters
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
print("Vowels:", v_count)
print("Consonants:", c_count)

''' output:
Enter a string: python
Vowels: 1
Consonants: 5 '''