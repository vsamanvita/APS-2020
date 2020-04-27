#Given n and different denominations of coins,returns number of differnt ways you can form 'n'
def coin_change(c,n):
	ways=[0]*(n+1)
	ways[0]=1
	for i in c:
		for j in range(i,n+1):
			ways[j]+=ways[j-i]
	return(ways[n])


n=4
denom=[1,2,3]
print(coin_change(denom,n))