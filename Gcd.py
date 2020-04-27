#Given x and y returns gcd of the numbers
#if gcd==1 x and y are co primes
def gcd(x, y): 
   while(y): 
       x, y = y, x % y 
   return x

res=(gcd(3,9))
print(res)
if res==1:
	print("Co-primes")
else:
	print("Not Co-primes")