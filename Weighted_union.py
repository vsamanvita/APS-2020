def root(arr,i):
	while arr[i]!=i:
		i=arr[i]
	return i


def find(arr,u,v):
	if root(arr,u)==root(arr,v):
		return 1
	else:
		return 0
		

def weigthed_union(arr,size,u,v):
	rootu=root(arr,u)
	rootv=root(arr,v)
	if size[rootu]<size[rootv]:
		arr[rootu]=arr[rootv]
		size[rootv]+=size[rootu]
	else:
		arr[rootv]=arr[rootu]
		size[rootu]+=size[rootv]


vertex=[0,1,2,3,4,5]
size=[1 for i in range(len(vertex))]
weigthed_union(vertex,size,0,1)
weigthed_union(vertex,size,1,2)
weigthed_union(vertex,size,3,2)

print(vertex)
print(size)