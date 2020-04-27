# Given a number n this codelet retuns the count where n+x=n^x where xE[0,n]

def sumXor(n):
    if n==0:
        return 1
    count=0
    l=int((math.log(n) / math.log(2)) + 1)
    n=n^((1<<l)-1)
    # print(n,l)
    while n:
        n=n&(n-1)
        count+=1

    return 2**count