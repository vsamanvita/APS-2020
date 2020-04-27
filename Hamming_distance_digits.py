# Program to determine hamming distance
def count_bits(n):#count set bits
	count=0
	while(n):
		n&=(n-1)
		count+=1
	return count

def hammingDistance(a,b):
	x=a^b #bit difference
	setb=count_bits(x)
	return(setb)

a=8
b=14
c=14
print(hammingDistance(a,b))
print(hammingDistance(c,b))