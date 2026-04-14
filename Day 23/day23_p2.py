# Find the Majority Element in an Array
# Find the element that appears more than n/2 times in the array (if any).
# Input: [3, 3, 4, 2, 4, 4, 2, 4, 4]
# Output: Majority Element: 4

arr = list(map(int, input("Enter numbers: ").split()))
for i in arr:
    if arr.count(i) > len(arr)//2:
        print("Majority Element:", i)
        break
else:
    print("No Majority Element")
    
# output:
# Enter numbers:  3 3 4 2 4 4 2 4 4              
# Majority Element: 4