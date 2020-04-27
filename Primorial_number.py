#Print nth primorial number
def SieveOfSundaram(n):
    primes=[]
    nNew=int((n-2)/2)
    marked=[0]*(nNew+1)
    for i in range(1,nNew+1): 
        j=i; 
        while((i+j+2*i*j)<=nNew): 
            marked[i+j+2*i*j] = 1 
            j+=1 
    if (n>2): 
        primes.append(2) 
    for i in range(1,nNew+1): 
        if (marked[i]==0):
            primes.append(2*i+1)
    return(primes)

t=10**6
p=SieveOfSundaram(t) #generate prime numbers less than t 

n=6
res=1
for i in range(n):
    res*=p[i]
print(res)
