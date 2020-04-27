#Prints all permutations of given array
def permute(arr,n):
	for j in range(1,n+1):
		for i in range(n-1):
			temp=arr[i]
			arr[i]=arr[i+1]
			arr[i+1]=temp
			for k in range(n):
				print(arr[k],end=" ")
			print()

a=[1,2,3]
permute(a,len(a))