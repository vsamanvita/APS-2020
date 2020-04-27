##union(a,b)->add b set to a
#find returns 1 if vertex a,b are in same set else returns 0 if in different
def find(arr,a,b):
	if arr[a]==arr[b]:
		return 1
	else:
		return 0

def union(arr,a,b):
	val=arr[b]
	replace=arr[a]
	for i in range(len(arr)):
		if arr[i]==replace:
			arr[i]=val

vertex=[0,1,2,3,4,5,6,7,8,9]
edge=[(2,1),(4,3),(8,4),(9,3),(6,5)]

for e in edge:
	union(vertex,e[0],e[1])

# print(vertex)
print(find(vertex,0,7))
print(find(vertex,8,9))