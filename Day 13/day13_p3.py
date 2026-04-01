# Program to Print Integers in Words:
# Write a program that converts each digit of an integer entered by the user into its corresponding word representation. For example:
# Input: Enter a number: 123
# Output: One Two Three

num = input("Enter a number: ")
words = {
    '0': "Zero", '1': "One", '2': "Two", '3': "Three",
    '4': "Four", '5': "Five", '6': "Six",
    '7': "Seven", '8': "Eight", '9': "Nine"
}
for digit in num:
    print(words[digit], end=" ")
    
# output:
# Enter a number: 345
# Three Four Five 