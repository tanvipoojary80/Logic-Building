'''Remove All Non-Alphabetic Characters
Remove all characters that are not letters.
Input: "abc123!@#"
Output: "abc"
'''

import re
text = input("Enter a string: ")
result = re.sub(r'[^a-zA-Z]', '', text)
print("Output:", result)

'''output:
Enter a string: abcd123@&
Output: abcd'''

