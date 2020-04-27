# Python3 program to find Kth smallest element in a gieven array
def kthSmallest(arr,k):

	arr1=list(set(arr))
	arr1.sort()
	# print(arr1)
	return arr1[k-1]

# print(kthSmallest([9,6,7,7,7,9,6,5,2,4],5))