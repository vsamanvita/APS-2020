#Implementation of stack

#Method 1
from queue import LifoQueue
maxsize=4
stack=LifoQueue()
i=1
#push
while stack.qsize()<maxsize:
	stack.put(i)
	i+=1
print("Size:",stack.qsize())

#pop
while stack.qsize()>0:
	print(stack.get())
print("Size:",stack.qsize())

#Method 2
from collections import deque 

stack = deque() 

#push
stack.append('a') 
stack.append(2) 
print('Initial stack:',stack) 

#pop
print(stack.pop()) 
print(stack.pop()) 

print('Stack after elements are popped:',stack) 
