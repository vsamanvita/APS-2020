#catalan number recursion
def catalan_res(n):
    if n<=1:
        return 1
    res=0
    for i in range(0,n):
        res+=catalan_res(i)*catalan_res(n-i-1)
    return(res)

n=int(input())
r=catalan_res(n)
print(r)