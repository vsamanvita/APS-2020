import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    t=(n-1)//3
    tsum=((t*(t+1))//2)*3
    t=(n-1)//5
    fsum=((t*(t+1))//2)*5
    t=(n-1)//15    
    fisum=((t*(t+1))//2)*15
    print(tsum+fsum-fisum)