#Prints Pascel's triangle for given n
def pascal_triangle(n):
	pascal=[]
	for i in range(n):
		pascal.append([])
		pascal[i].append(1)
		for j in range(1,i):
			c=pascal[i-1][j]+pascal[i-1][j-1]
			pascal[i].append(c)
		if i>0:
			pascal[i].append(1)
	return pascal

n=4
res=pascal_triangle(n)  
for i in res:
	print(*i)