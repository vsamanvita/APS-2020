from collections import deque 

#method1->Slicing
def left_rotate(a,r):
	r=r%len(a)
	a=a[r:]+a[:r]
	return(a)

#method2->deque
def left_rotate1(a,r):
	r=r%len(a)
	a=deque(a) 
	a.rotate(-r) 
	a=list(a)
	return(a)

a=[1,2,3,4,5]
r=19
res=left_rotate1(a,r)
print(res)