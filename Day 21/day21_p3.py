# Sum of the series of n terms Write a program to calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/n up to the nth term.
# Input: n = 4
# Output: 2.083333

n = int(input("Enter the value of n: "))
sum_series = 0
for i in range(1, n + 1):
    sum_series += 1 / i
print("Sum of the series:", sum_series)

# output:
# Enter the value of n: 5
# Sum of the series: 2.283333333333333