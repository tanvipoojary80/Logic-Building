# Print a Number in Reverse Order:
# Write a program where the user enters a number, and the program prints it in reverse order. For example:
# Input: 1234
# Output: 4321

num = int(input("Enter a number: ")) # Take input from user
reverse = 0 # Initialize reverse variable
while num > 0: # Reverse the number using while loop
    digit = num % 10 # Get last digit
    reverse = reverse * 10 + digit # Add digit to reverse
    num = num // 10 # Remove last digit from number
print("Reversed number:", reverse) # Display reversed number


# output 1:
# Enter a number: 654321
# Reversed number: 123456

# output 2:
# Enter a number: 7654398
# Reversed number: 8934567
