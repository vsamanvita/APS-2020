#converts an 2d array to 1D array
def convert(a):
	res=[]
	for i in a:
		if type(i)==list:
			res.extend(i)
		else:
			res.append(i)
	return(res)

a=[1,2,[3,4],[5],6,[7,8,9]]
res=convert(a)
print(res)