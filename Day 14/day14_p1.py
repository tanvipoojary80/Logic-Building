''' Print Numbers in Words in Reverse Order Using a Switch Case:
Write a program that takes an integer, reverses it, and prints each digit as a word using a switch case. For example:
Input: Enter a number: 321
Output: One Two Three '''

n = int(input("Enter a number: "))
rev = 0
# Reverse the number
while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
# Print digits in words using match-case
while rev != 0:
    digit = rev % 10
    match digit:
        case 0: print("Zero", end=" ")
        case 1: print("One", end=" ")
        case 2: print("Two", end=" ")
        case 3: print("Three", end=" ")
        case 4: print("Four", end=" ")
        case 5: print("Five", end=" ")
        case 6: print("Six", end=" ")
        case 7: print("Seven", end=" ")
        case 8: print("Eight", end=" ")
        case 9: print("Nine", end=" ")
    rev //= 10

''' output:
Enter a number: 987
Nine Eight Seven '''