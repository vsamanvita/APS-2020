#Given string s prints all substrings of s
def compute(arr,n):
	for l in range(1,n+1):
		for i in range(n-l+1):
			j=i+l-1;
			for k in range(i,j+1):
				print(arr[k],end=" ")
			print()

s="abc"
compute(s,len(s))
