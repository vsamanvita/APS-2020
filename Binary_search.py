#Given a sorted array and an element returns the index of the element if present else -1
def binary_search(a,l,r,x):
	if l<=r:
		mid=l+(r-l)//2
		if a[mid]==x:
			return mid
		elif a[mid]>x:
			return binary_search(a,l,mid-1,x)
		else:
			return binary_search(a,mid+1,r,x)
	else:
		return -1


a=[2,4,6,8,10]
print(binary_search(a,0,len(a)-1,11))