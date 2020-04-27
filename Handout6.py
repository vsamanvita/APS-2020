#Checks whether the sum(sm) of any subset is equal to the given sum
#equal->YES not equal->NO
def find(arr,l,s):
	flag=0
	for i in range(1,pow(2,l)):
		sm=0
		for j in range(0,l):
			if (i>>j)&1:
				sm+=arr[j]
		if sm==s:
			print("YES")
			flag=1
	if flag==0:
		print("NO")
	return
#ex1
sm=128
n=4
arr=[-1,2,4,121]
find(arr,n,sm)
#ex2
sm=6
n=4
arr=[-1,2,4,121]
find(arr,n,sm)