# Using recursion to find maximum value

#List of values to operate on
items = [1,2,3,12,54,14,100,43,99]

def find_max(items):
    #If it is the only item in a list, return it
    if len(items) ==1:
        return items[0]
    #Otherwise get the first item and call the function again to operate on the rest of the list
    item1 = items[0]
    item2 = find_max(items[1:])
    #Perform the comparison again when we're down to only two
    if item1 > item2:
        return item1
    else:
        return item2

print(find_max(items))