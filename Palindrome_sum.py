#Given n,returns sum of all n digit palindromes.
import math
def palindrome_sum(n):
	sum=0
	if n==1:
		return 45
	else:
		sum=(99.0/2.0)*pow(10,(n-1))*pow(10,math.floor((n-1)/2))
	return sum

print(int(palindrome_sum(8)))

