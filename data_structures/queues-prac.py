# Practicing ques implementation in Python

from collections import deque #optimized queue implementation

#Creating a queue
queue = deque()

# Adding items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)

#Remove items from the queue
queue.popleft()
print(queue)

