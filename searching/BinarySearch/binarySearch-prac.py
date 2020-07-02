# Binary search practice
items = [5,34,12,45,66,77,85,23,12,98]

# Sort the items first
items.sort()


def binarySearch(item, itemsList):
    #Define the lower index as the first item
    lowerIndex = 0
    #define the upper index as the last item
    upperIndex = len(itemsList) -1
    
    #execute till the indexes cross
    while lowerIndex <= upperIndex:
        #calculate the midpoint
        midpoint = (upperIndex + lowerIndex) // 2
        #if item is found at midpoint, return it
        if itemsList[midpoint] == item:
            return midpoint
        #If item is not found, advance the lower and upper index
        if item > itemsList[midpoint]:
            lowerIndex = midpoint +1
        else:
            upperIndex = midpoint -1
    
    #if points cross, then the item is not found
    if lowerIndex >= upperIndex:
        return None
         
print(binarySearch(23,items))
print(binarySearch(200, items))