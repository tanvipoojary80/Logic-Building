'''Check Palindrome
Determine if a string reads the same backward as forward.
Input: "madam"
Output: "Palindrome"
'''
text = input("Enter a string: ")
rev = text[::-1]
if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
    
'''output:
Enter a string: mom
Palindrome'''
