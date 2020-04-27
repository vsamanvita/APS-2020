#Calculating Binomial using recursion
#nCk
def bc(n,k):
    if n==k or k==0:
        return 1
    return bc(n-1,k-1)+bc(n-1,k)
n=int(input())
k=int(input())
c=bc(n,k)
print(c)