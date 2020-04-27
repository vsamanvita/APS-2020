# Prints largest Product in subarray
import sys

t = int(input().strip())
for a0 in range(t):
    n,k = map(int,input().split())
    num = input().strip()
    a=[int(i) for i in list(num)]
    p=1
    pp=1
    for i in range(k):
        p*=a[i]
    mx=p 
    j=0
    for i in range(k,len(a)):
        p=1
        aa=a[j+1:i+1]
        for i in range(k):
            p*=aa[i]
        mx=max(mx,p)
        j+=1
    print(int(mx))