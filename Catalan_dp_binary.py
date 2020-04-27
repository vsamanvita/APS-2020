#catalan number DP
# How many structurally different binary trees are possible with n nodes?
# DP approach
# Eg:n(number of nodes)=3, result = 5
def catalan(n):
    c=[0 for i in range(0,n+1)]
    c[0]=1
    c[1]=1
    c[2]=2
    for i in range(3,n+1):
        for j in range(i):
            c[i]+=c[j]*c[i-1-j]
    return(c[n])
n=int(input())
r=catalan(n)
print(r)