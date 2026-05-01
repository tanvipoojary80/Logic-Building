'''2. Merge Two Dictionaries
Task: Combine the items of two dictionaries into a single new dictionary.
Input:
dict1 = {"name": "John", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
Expected Output:
{'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}
'''

dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))
merged = dict1 | dict2
print("Merged dictionary:", merged)

'''output:
Enter first dictionary: {"name": "John", "age": 25}
Enter second dictionary: {"city": "New York", "country": "USA"}
Merged dictionary: {'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}
'''