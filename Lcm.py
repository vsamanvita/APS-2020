#Given 2 numbers a,b returns Lcm a,b
def lcm(a,b):
	l=max(a,b)
	s=min(a,b)
	i=l
	while(1):
		if i%s==0:
			return i
		i+=l


print(lcm(15,20))