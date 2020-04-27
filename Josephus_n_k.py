#Josephus Problem given n,k
n,k=map(int,input().split())
res=0
for i in range(1,n+1):
    res=(res+k)%i
print(res+1)