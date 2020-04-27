# Program to find all primes smaller than or equal to n

def SieveOfEratosthenes(n):
	prime=[True for i in range(n+1)]
	sol=[]
	p=2
	while p*p<=n:
		if prime[p]==True:
			for i in range(p*p,n+1,p):
				prime[i]=False
		p+=1
	
	# print(prime)
	for p in range(2,n):
		if prime[p]:
			sol.append(p)

	return sol


# print(SieveOfEratosthenes(30))
