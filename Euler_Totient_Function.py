#Calculates Euler Totient 
#prints the count of number in range 1 to n that are relatively prime to n
#i.e. co-prime with n

def phi(n):
	res=n
	i=2
	while(i*i<=n):
		if n%1==0:
			while n%i==0:
				n/=i
			res-=int(res/i)
		i+=1
	if n>1:
		res-=int(res/n)
	return res

print(phi(40))