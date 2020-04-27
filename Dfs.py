#DFS Algorithm
#prits the traversed path
vertex=[0,1,2,3,4,5,6]
edge=[(0,1),(0,2),(1,0),(1,3),(2,0),(2,4),(2,5),(3,1),(4,2),(4,6),(5,2),(6,4)]

adj=[[] for i in vertex]

for i in range(len(edge)):
	adj[edge[i][0]].append(edge[i][1])

visited=[]
stack=[vertex[0]]

while len(stack)>0:
	root=stack.pop()
	for node in adj[root]:
		if node not in visited:
			stack.append(node)
	visited.append(root)
#Tranversed path
print(visited)
