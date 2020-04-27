n=int(input())
a=[]
c=[chr(x) for x in range(ord('A'),ord('Z')+1)]
for i in range(n):
    name=input()
    a.append(name)
a.sort()
# print(a)
q=int(input())
for _ in range(q):
    fn=input()
    ind=a.index(fn)+1
    # print(ind)
    s=0
    for i in fn:
        s+=c.index(i)+1
    s=s*ind
    print(s)