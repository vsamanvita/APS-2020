#tribonacci sequence
#prints first n terms of a tribonacci sequence
def tribonacci(n):
    seq=[0,0,1]
    for i in range(n-3):
        seq.append(seq[-1]+seq[-2]+seq[-3])
    return(seq)

n=10
if n==1:
    print(0)
elif n==2:
    print(0,0)
res=tribonacci(n)
print(res)