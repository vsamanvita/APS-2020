#Given an array print all subsets of it i.e (2^n)-1 subsets
def calc(a,n):
	for i in range((1<<n)):
		for j in range(n):
			if i&(1<<j):
				print(a[j],end=" ")
		print()

arr=['a','b','c']
calc(arr,len(arr))
