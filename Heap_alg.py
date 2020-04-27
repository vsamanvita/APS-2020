def heap(h):
	n=len(h)-1
	for i in range(n//2,0,-1):
		k=i
		v=h[i]
		heap=False
		while not heap and 2*k<=n:
			j=2*k
			if j<n:
				if h[j]<h[j+1]:
					# h[j]=h[j+1]
					j+=1
			if v>=h[j]:
				heap=True
			else:
				h[k]=h[j]
				k=j
		h[k]=v

h=[0,2,9,7,6,5,8]
heap(h)
print(h[1:])
