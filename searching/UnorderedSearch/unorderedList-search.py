'''
- Searching unordered list has a perfomance O(n) hence can be inneficient.

'''

items = [5,34,12,45,66,77,85,23,12,98]

def search(item,itemsList):
    for i in range(len(itemsList)):
        if itemsList[i] == item:
            return i
    return None


print(search(85,items))
print(search(200, items))