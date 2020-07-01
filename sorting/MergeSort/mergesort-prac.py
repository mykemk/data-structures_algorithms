
# A list of unsorted items
items = [2,3,78,12,34,15,10,30]

def mergeSort(dataset):
    if len(dataset) >1:
        middle_of_array = len(dataset) // 2
        leftArray = dataset[:middle_of_array] #get the left half of the array
        rightArray = dataset[middle_of_array:] #get the right half of the array

        # Recursively break the array into small parts
        mergeSort(leftArray)
        mergeSort(rightArray)

        #Compare and merge the left and right array
        i = 0 #index into the left array
        j = 0 #index into the right array
        k = 0 #index into the final merged array
        while i <len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                dataset[k] = leftArray[i]
                i+=1
            else:
                dataset[k] = rightArray[j]
                j+=1
            k+=1
        #If the left array still has values, include them
        while i< len(leftArray):
            dataset[k] = leftArray[i]
            i+=1
            k+=1
        
        #if the right array still has valulues, inlude them
        while j<len(rightArray):
            dataset[k] = rightArray[j]
            j+=1
            k+=1

print(items)
mergeSort(items)
print(items)

