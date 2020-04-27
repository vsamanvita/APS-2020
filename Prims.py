maxint=999999999

def minKey(key,mstSet):
	minx=maxint 
	for v in range(V): 
		if key[v]<minx and mstSet[v]==False: 
			minx=key[v] 
			min_index=v 

	return min_index 

def primMST(graph,V): 
	key=[maxint]*V 
	parent=[None]*V 
	key[0]=0
	mstSet=[False]*V 

	parent[0]=-1 
	for cout in range(V):
		u=minKey(key,mstSet)
		mstSet[u]=True 
		for v in range(V):
			if graph[u][v]>0 and mstSet[v]==False and key[v]>graph[u][v]: 
					key[v]=graph[u][v] 
					parent[v]=u 

	return(parent) 


V=5
graph = [[0, 2, 0, 6, 0],[2, 0, 3, 8, 5],[0, 3, 0, 0, 7],[6, 8, 0, 0, 9],[0, 5, 7, 9, 0]]
parent=primMST(graph,V)
print("Edge \t Weight")
for i in range(1,V): 
	print(parent[i],"-",i,"\t ",graph[i][parent[i]]) 
