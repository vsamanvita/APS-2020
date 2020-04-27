#returns whether a number has odd or even number of factors
#Odd->odd number of factors,Even->even number of factors
import math
def odd_even(n):
	v=int(math.sqrt(n))
	if n/v==1 or n/v==v:
		return"Odd"
	return"Even"

print(odd_even(2))
print(odd_even(169))