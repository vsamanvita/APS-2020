#Construction sparse table
#query
lookup=[[0 for i in range(10)]for j in range(10)]
def sparse_table(a,n):
    global lookup
    j=1
    while (1<<j)<=n:
        i=0
        while (i+(1<<j)-1)<n:
            if(a[lookup[i][j-1]]<a[lookup[i+(2**(j-1))][j-1]]):
                lookup[i][j]=lookup[i][j-1]
            else:
                lookup[i][j]=lookup[i+(2**(j-1))][j-1]
            i+=1
        j+=1

def query(a,L,R):
    j=math.log((R-L+1),2)
    if(a[lookup[L][j]]<=a[lookup[R-(2**j)+1][j]]):
        return a[lookup[L][j]]
    else:
        return a[lookup[R-(2**j)+1][j]]
    
    
n=int(input())
a=[int(i) for i in input().split()]
for i in range(n):
    lookup[i][0]=i
sparse_table(a,n)
print(lookup)