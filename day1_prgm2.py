#Write a Program to Find the Size of int, float, double, and char on Your Computer:
#Write a program that displays the size of fundamental data types (int, float, double, and char) on your system. For example:
#Output:
#Size of int: 4 bytes
#Size of float: 4 bytes
#Size of double: 8 bytes
#Size of char: 1 byte

import sys
a = 10
b = 10.5
c = 'A'
print("Size of int:", sys.getsizeof(a), "bytes")
print("Size of float:", sys.getsizeof(b), "bytes")
print("Size of char:", sys.getsizeof(c), "bytes")
