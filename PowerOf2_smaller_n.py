#prints nearest powe of 2 less than n
#Method1->bitwise

n=103
k=len(bin(n))-2
val=1
val=val<<k-1
print(val)
	

# Method2
def near_power(n):
	res=0
	for i in range(n,0,-1):
		if((i&(i-1)))==0:
			res=i
			break
	return(res)

n=1023
print(near_power(n))