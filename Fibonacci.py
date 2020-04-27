#fibonacci sequence
#prints first n terms of a fibonacci sequence
def fibonacci(n):
    seq=[0,1]
    for i in range(n-1):
        seq.append(seq[-1]+seq[-2])
    return(seq[1:])

n=5
res=fibonacci(n)
print(res)