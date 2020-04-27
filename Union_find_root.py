#root means the index and its value is the same
def root(arr,i):
	while arr[i]!=i:
		i=arr[i]
	return i

def find(arr,u,v):
	if root(arr,u)==root(arr,v):
		return 1
	else:
		return 0

def union(arr,u,v):
	rootu=root(arr,u)
	rootv=root(arr,v)
	arr[rootu]=rootv

vertex=[0,1,2,3,4,5,6,7]
edges=[(0,1),(0,5),(3,4),(5,3),(1,6)]
for edge in edges:
	union(vertex,edge[0],edge[1])
print(vertex)
print(find(vertex,1,5))

