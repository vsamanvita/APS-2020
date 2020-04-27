#Prints the topological sort of the given graph
from collections import defaultdict

n=6
vertex=[i for i in range(n)]
edge=[(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]
adj=defaultdict(list)

for i in range(len(edge)):
	adj[edge[i][0]].append(edge[i][1])

def topo(v,visited,stack):
	global adj
	visited[v]=True
	for i in adj[v]:
		if visited[i]==False:
			topo(i,visited,stack)
	stack.insert(0,v)

def topological_sort(n):
	visited=[False]*n
	stack=[]

	for i in range(n):
		if visited[i]==False:
			topo(i,visited,stack)
	return(stack)

res=topological_sort(n)
#topological sort
print(*res)