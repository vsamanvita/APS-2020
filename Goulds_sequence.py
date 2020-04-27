def gould(n):
	seq=[]
	for j in range(1,n+1):
		ct=1
		c=1
		for i in range(1,j):
			c=c*(j-i)/i
			if c%2==1:
				ct+=1
		seq.append(ct)
	return(seq)

n=8
res=gould(n)
print(*res)
