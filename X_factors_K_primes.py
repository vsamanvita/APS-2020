#prints whether a valid +ve integer exists with 'x' factors and 'k' prime among them
#NO->integer doesn't exist,YES->integer exists
import math

t=int(input())
for _ in range(t):
    x,k=map(int,input().split())
    if x==1 and k==0:
        print(1)
    else:
        a=[]
        for i in range(2,int(math.sqrt(x))+1):
            while x%i==0:
                a.append(i)
                x=x/i
        if x>1:
            a.append(x)
        # print(a)
        if len(a)<k:
            print("NO")
        else:
            print("YES")

