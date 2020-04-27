#Prints first n polite numbers.
import math
def polite(n):
	ct=1
	i=2
	a=[1]
	while ct<n:
		res=math.log(i,2)
		if not res.is_integer():
			ct+=1
			a.append(i)
		i+=1
	return(a)



n=12
res=polite(n)
print(*res)
