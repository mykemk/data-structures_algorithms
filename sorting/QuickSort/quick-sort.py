
items = [12,5,6,7,78,45,2,3,12,34]

def partition(datavalues, first, last):
    #Selects the first item to be the pivot index
    pivotIndex = first
    #set the lower index
    lowerIndex = first +1 #The second item set to be the lower index 
    #Set the index of the uper item
    upperIndex = last #the last item set to be the upper index

    # Compare the values to check for the crossing point
    done = False

    while not done:
        #advance the lower index
        while lowerIndex <= upperIndex and datavalues[lowerIndex] <= datavalues[pivotIndex]:
            #advance the upper index
            lowerIndex +=1
        while upperIndex >= lowerIndex and datavalues[upperIndex] >= datavalues[pivotIndex]:
            upperIndex -=1
        #if the points cross, we have found the split point
        if upperIndex < lowerIndex:
            done = True
        else:
            temp = datavalues[lowerIndex]
            datavalues[lowerIndex] = datavalues[upperIndex]
            datavalues[upperIndex] = temp

    #when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upperIndex]
    datavalues[upperIndex] = temp

    return upperIndex

def quickSort(dataset,first, last):
    if first < last:
        #calculate the split point
        pivotIdx = partition(dataset,first,last)
        #sort the two partitions
        quickSort(dataset,first, pivotIdx)
        quickSort(dataset,pivotIdx+1,last)

print(items)
quickSort(items,0,len(items) -1)
print(items)