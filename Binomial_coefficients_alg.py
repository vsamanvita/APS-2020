#Binomial Coefficient algorithm
n=int(input())
k=int(input())
c=[[0 for i in range(k+1)]for j in range(n+1)]
for i in range(0,n+1):
    for j in range(0,min(i,k)+1):
        if i==j or j==0:
            c[i][j]=1
        else:
            c[i][j]=c[i-1][j]+c[i-1][j-1]
print(c[n][k])