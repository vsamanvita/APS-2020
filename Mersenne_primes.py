#prints mersenne numbers less than n
#mersenne no->2^p-1 is prime
def SieveOfEratosthenes(n, prime):
	for i in range(0,n+1) :
		prime[i]=True
	p=2
	while(p*p<=n):
		if (prime[p]==True) : 
			for i in range(p*2,n+1,p): 
				prime[i] = False		
		p += 1
		
def mersennePrimes(n) : 
	prime=[0]*(n+1)
	SieveOfEratosthenes(n, prime) 
	k=2
	while(((1<<k)-1)<=n): 
		num=(1<<k)-1
		if (prime[num]) : 
			print(num,end= " ") 
			
		k+=1
	 
n=10000000
mersennePrimes(n) 
