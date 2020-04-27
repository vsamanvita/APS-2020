#Selection sort
def selection_sort(a):
	for i in range(len(a)):
		min_idx = i 
		for j in range(i+1,len(a)): 
			if a[min_idx] > a[j]: 
				min_idx = j
		a[i], a[min_idx] = a[min_idx], a[i] 


arr=[5,3,8,9,6,1,0,5,3,9,10,8,12,11]
selection_sort(arr)
print(arr)