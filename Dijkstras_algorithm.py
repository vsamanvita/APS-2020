#given number of vertices,soucre and adjacency matrix(distance between nodes)
#finds shortest distance from source to each vertex
maxint=999999999

class Graph(): 

	def __init__(self,vertices): 
		self.V=vertices 
		self.graph=[[0 for column in range(vertices)]for row in range(vertices)] 

	def minDistance(self,dist,sptSet): 
		min=maxint 
		for v in range(self.V): 
			if dist[v]<min and sptSet[v]==False: 
				min=dist[v] 
				min_index=v 
		return min_index 

	def dijkstra(self,src):
		global maxint
		dist=[maxint]*self.V 
		dist[src]=0
		sptSet=[False]*self.V 
		for cout in range(self.V): 
			u=self.minDistance(dist, sptSet)
			sptSet[u]=True
			for v in range(self.V): 
				if self.graph[u][v]>0 and sptSet[v]==False and dist[v]>dist[u]+self.graph[u][v]: 
						dist[v]=dist[u]+self.graph[u][v] 

		return(dist) 

#number of vertexes
v=9
g=Graph(v) 
g.graph=[[0, 4, 0, 0, 0, 0, 0, 8, 0], 
		[4, 0, 8, 0, 0, 0, 0, 11, 0], 
		[0, 8, 0, 7, 0, 4, 0, 0, 2], 
		[0, 0, 7, 0, 9, 14, 0, 0, 0], 
		[0, 0, 0, 9, 0, 10, 0, 0, 0], 
		[0, 0, 4, 14, 10, 0, 2, 0, 0], 
		[0, 0, 0, 0, 0, 2, 0, 1, 6], 
		[8, 11, 0, 0, 0, 0, 1, 0, 7], 
		[0, 0, 2, 0, 0, 0, 6, 7, 0] ]; 


source=0
dist=g.dijkstra(source); 
for i in range(v):
	print("Distance from source ",source,"to vertex ",i,"is:",dist[i])