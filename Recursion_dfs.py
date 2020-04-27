#DFS implementation using recursion
from collections import defaultdict

n=4
vertex=[0,1,2,3] #as n is 4
edge=[(0, 1),(0, 2),(1, 2),(2, 0),(2, 3),(3, 3)]
adj=defaultdict(list)


for i in range(len(edge)):
	adj[edge[i][0]].append(edge[i][1])
# print(adj)

visited=[]

def dfs(adj,n,source):
	visited.append(source)
	for i in range(n):
		if vertex[i] in adj[source]:
			if vertex[i] not in visited:
				print(i,end=" ")
				dfs(adj,n,i)

source=vertex[2]
print(source,end=" ")
dfs(adj,len(vertex),source)