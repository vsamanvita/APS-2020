#Given a matrix prints the absolute difference between upper and lower triangles/bounds.
def bound_difference(a):
	usum=0
	lsum=0
	for i in range(len(a)):
		for j in range(len(a[i])):
			if i>j:
				lsum+=a[i][j]
			if i<j:
				usum+=a[i][j]
	print(abs(usum-lsum))

a=[[1,3,3],[1,2,3],[1,1,3]]
bound_difference(a)