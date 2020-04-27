#Minimum cost assignment Problem using bitwise and dp
# Given n jobs ,n workers' cost to do the job, find the minimal cost 
n=3
cost=[[3,2,7],[5,1,3],[2,7,2]]
dp=[float("inf") for i in range(2**n)]
dp[0]=0

def count_b(n):
    count=0
    while(n):
        n=n&(n-1)
        count+=1
    return(count)
    
for mask in range(0,2**n):
    x=count_b(mask)
    for j in range(0,n):
        setb=mask&(1<<j)
        if setb==0:
            bit=mask|(1<<j)
            dp[bit]=min(dp[bit],dp[mask]+cost[x][j])
print(dp[2**n-1])