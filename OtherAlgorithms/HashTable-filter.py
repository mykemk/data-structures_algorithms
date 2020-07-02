'''
Since Hash tables keys have to be unique, they can be used to filter unique values in a list
- Loop through the list of items
- Add all the items in a list as keys in the hash table
- Obtain the keys in the created hash tables
- Has a time complexity of O(n) since the time increases as the item list grows
'''
# Using hash tables to filter out unique items

fruits = ["Mango", "Bananan", "apple", "Mango", "Orange", "Orange", "grapes"]

def filterUnique(items):
    filtered = dict()
    for item in items:
        filtered[item] = 0
        
    return list(filtered.keys())
    
print(filterUnique(fruits))