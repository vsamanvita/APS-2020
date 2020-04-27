#Find the sum of the digits in the number n!
a=[1]
p=1
for i in range(1,1001):
    p*=i
    a.append(p)
t=int(input())
for _ in range(t):
    n=int(input())
    l=[int(x) for x in str(a[n])]
    print(sum(l))