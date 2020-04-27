#BFS Algorithm
#prits the traversed path
vertex=[0,1,2,3,4,5,6]
edge=[(0,1),(0,2),(1,0),(1,3),(2,0),(2,4),(2,5),(3,1),(4,2),(4,6),(5,2),(6,4)]

adj=[[] for i in vertex]

for i in range(len(edge)):
	adj[edge[i][0]].append(edge[i][1])

visited=[]
queue=[vertex[0]]

while len(queue)>0:
	root=queue.pop()
	for node in adj[root]:
		if node not in visited:
			queue.insert(0,node)
	visited.append(root)
#Tranversed path
print(visited)