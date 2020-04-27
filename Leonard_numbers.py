#Leonard_numbers
#prints first n terms of a sequence
def leonardo(n):
    seq=[1,1]
    for i in range(n-2):
        seq.append(seq[-1]+seq[-2]+1)
    return(seq)

n=10
res=leonardo(n)
print(res)