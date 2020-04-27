# Program to determine the number of bits set in a number using bitwise ops.
def count_bits(n):
	count=0
	while(n):
		n&=(n-1)
		count+=1
	return count

n=91456
print(count_bits(n))

#Method 2
print(bin(n).count('1'))