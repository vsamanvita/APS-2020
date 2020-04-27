#t->testcases,n->no of different coin denominations,l->list of coin denomination
# p->cost
#prints whether a person has to over pay or not
#NO->need not pay extra irrespective of cost
#YES->pays extra and also prints one condition
t=int(input())
for k in range(t):
    np=list(map(int,input().split()))
    n=np[0]
    p=np[1]
    l=[0 for i in range(n)]
    flag=0
    d=list(map(int,input().split()))
    x=d.copy()
    for i in range(len(d)):
        if p%d[i]!=0:
            flag=1
            mul=-(-p//d[i])
            l[i]=mul
            break
    if flag==0:
        for i in range(n-1,0,-1):
            if x[i]%x[i-1]!=0:
                flag=2
                ii=i
                break
        if flag==2:
            mul=p//d[ii]-1
            l[ii]=mul
            mul=(p-(mul*d[ii]))//d[ii-1]+1
            l[ii-1]=mul
            print("YES",end=' ')
            print(*l)
        else:
            print("NO")
    else:
        print("YES",end=' ')
        print(*l)