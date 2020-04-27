#Prints all permutation of given string using recursion
def swap(a,x,y):
	temp=a[x]
	a[x]=a[y]
	a[y]=temp

def compute(a,l,r):
	if l==r:
		print("".join(a))
	else:
		for i in range(l,r+1):
			swap(a,l,i)
			compute(a,l+1,r)
			swap(a,l,i)

s="abcd"
n=len(s)
compute(list(s),0,n-1)
