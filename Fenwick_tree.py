#Fenwick Tree or Binary Indexed Tree
n=10;
bit=[0 for i in range(n+1)]

def update(ind,val):
    global n
    global bit
    while(ind<=n):
        bit[ind]+=val
        ind+=ind&-ind
    
def query(x):
    global n
    global bit
    sm=0
    while(x>0):
        sm+=bit[x]
        x-=x&-x
    return(sm)

a=[1]*(n)
for i in range(n):
    update(i+1,a[i])
    
print(query(5))
print(query(4))
print(query(10))
# print(bit)