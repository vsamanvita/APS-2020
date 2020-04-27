#Given a pair product array prints the original array
import math

def construct(pair,n):
	size=int((1+math.sqrt(1+8*n))//2);
	arr=[0 for i in range(size)]
	arr[0]=int(math.sqrt((pair[0]*pair[1])/pair[size-1]));
	for i in range(1,size):
		arr[i]=pair[i-1]//arr[0];
	return(arr)

pair=[48,18,24,24,32,12]
res=construct(pair,len(pair))
print(res)