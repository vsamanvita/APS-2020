#prints hamiltonian cycle for a given graph else -1 if path doesn't exist

def isSafe(v,pos,path):
	global graph
	if graph[path[pos-1]][v]==0: 
		return False 
	for vertex in path: 
		if vertex==v: 
			return False
	return True

def hamCycleUtil(path,pos):
	global V
	global graph 
	if pos==V:  
		if graph[path[pos-1]][path[0]]==1: 
			return True
		else: 
			return False
	for v in range(1,V): 
		if isSafe(v,pos,path)==True: 
			path[pos]=v 
			if hamCycleUtil(path,pos+1)==True: 
				return True 
			path[pos]=-1
	return False

def hamCycle():
	global V
	path=[-1]*V 
	path[0]=0

	if hamCycleUtil(path,1)==False: 
		print(-1)
	else:
		print(*path,path[0])

V=5
graph=[[0, 1, 0, 1, 0],[1, 0, 1, 1, 1],[0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],[0, 1, 1, 1, 0]] 
hamCycle()

graph=[[0, 1, 0, 1, 0],[1, 0, 1, 1, 1],[0, 1, 0, 0, 1,],[1, 1, 0, 0, 0],[0, 1, 1, 0, 0]] 
hamCycle()
