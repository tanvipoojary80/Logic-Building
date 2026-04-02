'''Amstrong Number or Not:
Write a program to check if a number is an Armstrong number. For example:
Input: Enter a number: 153
Output: 153 is an Armstrong number.
'''

n = int(input("Enter a number: "))
original = n
# Count number of digits
count = len(str(n))
sum = 0
# Calculate sum of powers
while n != 0:
    digit = n % 10
    sum += digit ** count
    n //= 10
# Check Armstrong
if sum == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")
    
'''output 1:
Enter a number: 123                
123 is not an Armstrong number
'''

'''output 2:
Enter a number: 370
370 is an Armstrong number
'''