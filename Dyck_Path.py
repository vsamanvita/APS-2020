#dyck path
#Prints all valid paths and total number of paths for given 'n'.
def dyck(n):
    li=['x' for i in range(n)]+['y' for i in range(n)]
    from itertools import permutations
    from collections import Counter
    count=0
    print("Valid Paths:")
    for i in set(permutations(li,n*2)):
        flag=0
        a=''.join(i)
        if a[0]=='x':
            for j in range(1,n*2):
                b=a[0:j]
                b=list(b)
                c=dict(Counter(b))
                if c['x']!=j:
                    if c['x']<c['y']:
                        flag=flag+1
            if flag==0:
                print(a)
                count=count+1
    return(count)

n=int(input()) # max x,y value
res=dyck(n)
print("Total Valid Paths:",res)