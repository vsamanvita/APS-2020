#implementing Queue using deque
#add element at end and delete at last
from collections import deque
q=deque([32,28])
print(q)
q.append(1)
print(q)
q.append(55)
print(q)

# O(1) for popping 0th index element
print(q.popleft())
print(q)