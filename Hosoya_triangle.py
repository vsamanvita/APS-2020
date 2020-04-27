def hosoya(n):
	dp=[[0 for i in range(n)]for i in range(n)]
	dp[1][0]=dp[1][1]=dp[0][0]=1
	for i in range(2,n):
		for j in range(n):
			if i>j:
				dp[i][j]=dp[i-1][j]+dp[i-2][j]
			else:
				dp[i][j]=dp[i-1][j-1]+dp[i-2][j-2]

	return(dp)

n=9
dp=hosoya(n)
for i in range(n):
	for j in range(i+1):
		print(dp[i][j],end=" ")
	print()