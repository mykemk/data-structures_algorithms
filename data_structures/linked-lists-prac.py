# Linked List practice

# The node class

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def set_data(self,data):
        self._value = data

    def set_next(self,next_node):
        self._next = next_node

    def get_data(self):
        return self._value
    def get_next(self):
        return self._next

class LinkedList:
    def __init__(self, head=None):
        self._head = head
        self._count = 0
    
    def get_count(self):
        return self._count
    
    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self._head)
        self._head = new_node
        self._count += 1 
    
    def find(self,value):
        item = self._head
        while(item!=None):
            if(item.get_data() ==value):
                return item
            else:
                item = item.get_next()
        return None;

    def deleteAt(self,index):
        if index > self._count -1:
            print('Sorry! item does not exist, Check the item position provided')
            return
        if index == 0:
            self._head = self._head.get_next()
        else:
            tempIndex = 0;
            node = self._head
            while tempIndex > index -1:
                node = node.get_next()
                tempIndex +=1
            node.set_next(node.get_next().get_next())
            self._count -=1


    
    def dump_list(self):
        current_node = self._head
        while(current_node !=None):
            print(f'Node: {current_node.get_data()}')
            current_node = current_node.get_next()
    

itemsList = LinkedList()
itemsList.insert(10)
itemsList.insert(15)
itemsList.insert(20)
itemsList.dump_list()

print(f'Item count: {itemsList.get_count()}')
print(f'Found item: {itemsList.find(10)}')
print(f'Found item: {itemsList.find(20)}')

itemsList.deleteAt(2)
itemsList.dump_list()
print(f'Item count: {itemsList.get_count()}')
itemsList.deleteAt(5)

