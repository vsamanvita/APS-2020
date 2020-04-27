import math
def prime_fact(n):
	f=[]
	flag=0
	while(n%2==0):
		flag=1
		n//=2
	if flag==1:
		f.append(2)
	for i in range(3,int(math.sqrt(n)+1)):
		if n%i==0:
			f.append(i)
			n//=i
	if n>2:
		f.append(n)
	return f

n=42
print(prime_fact(n))