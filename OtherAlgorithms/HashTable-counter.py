'''
Hash tables used to count item occurences in a list:
- Create a new hash table to hold the count values
- Loop over each item in a list
- If item exists, increament the counter
- If item does not exist, create it and initialise a value of one
'''

fruits = ["mango", "banana", "apple", "mango", "orange", "orange", "grapes"]

def count(items):
    # Hash table to hold items count
    itemsCount = dict()
    #check if item in the list exists
    for item in items:
        #if item exists, increase the count
        if item in itemsCount.keys():
            itemsCount[item] +=1
        #If item does not exist, initiate the count to one
        else:
            itemsCount[item] = 1
            
    return itemsCount
        
print(count(fruits))
