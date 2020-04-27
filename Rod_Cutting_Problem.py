#Rod Cutting Problem
#Print maximum price obtained by cutting rod into different length of pieces.
min_val=-99999
def cutRod(price,n):
    val=[0 for i in range(n+1)]
    for i in range(1,n+1):
        mx=min_val
        for j in range(i):
            mx=max(mx,price[j]+ val[i-j-1])
        val[i]=mx
    return val[n]

n=int(input())#length of rod
a=[int(i) for i in input().split()]# price for different lengths of rod <=n
res=cutRod(a,len(a))
print("Maximum Value:",res)