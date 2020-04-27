#Padovan sequence
#prints first n terms of a tribonacci sequence
def padovan(n):
    seq=[1,1,1]
    for i in range(4,n):
        seq.append(seq[-2]+seq[-3])
    return(seq)

n=3
if n==1:
    print(1)
elif n==2:
    print(1,1)
res=padovan(n)
print(res)