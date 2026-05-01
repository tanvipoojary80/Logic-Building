'''1. Dictionary Keys and Values
Task: Extract and print all the keys and values of a dictionary as separate lists.
Input:
data = {"name": "John", "age": 25, "city": "New York"}
Expected Output:
Keys: ["name", "age", "city"], Values: ["John", 25, "New York"]
'''

data = {}
n = int(input("Enter number of items: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value
keys = list(data.keys())
values = list(data.values())
print("Keys:", keys)
print("Values:", values)

'''output:
Enter number of items: 2
Enter key: name
Enter value: sam
Enter key: age
Enter value: 20
Keys: ['name', 'age']
Values: ['sam', '20']'''