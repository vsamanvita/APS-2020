#numbers of ways to reach a number by summing 3,5,10
# The Coin Change Problem
# Eg. 15 => (3+3+3+3+3),(5+5+5),(10+5). 
def calculate(c,n):
    for i in range(c,n+1):
        k=i-c
        if a[k]>0:
            a[i]=a[i]+a[k]
    
c=[3,5,10]
n=int(input())
a=[0 for i in range(n+1)]
a[0]=1
for j in c:
    calculate(j,n)
    
print(a[-1])