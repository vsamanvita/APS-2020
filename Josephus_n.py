#josephus problem given n
def checkp(n):
    pw=0
    for i in range(n,0,-1):
        if (i&(i-1))==0:
            pw=i
            break
    return(pw)
n=int(input())
p=checkp(2*n)
print(2*n-p+1)