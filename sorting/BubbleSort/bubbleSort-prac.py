
def bubbleSort(dataset):
    for i in range(len(dataset) -1, 0,-1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
        print('Current state:', dataset)


def main():
    myList = [6,23,45,66,12,2]
    bubbleSort(myList)
    print('Results: ', myList)

if __name__=='__main__':main()