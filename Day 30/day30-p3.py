'''3. Swap Keys and Values
Task: Create a new dictionary where the original keys become values and the original values become keys (Dictionary Comprehension).
Input:
data = {"name": "John", "age": 25, "city": "New York"}
Expected Output:
{'John': 'name', 25: 'age', 'New York': 'city'}
'''

data = eval(input("Enter dictionary: "))
swapped = {value: key for key, value in data.items()}
print("Swapped dictionary:", swapped)

'''output:
Enter dictionary:  {"name": "Sam", "age": 25, "city": "US"}             
Swapped dictionary: {'Sam': 'name', 25: 'age', 'US': 'city'}
'''