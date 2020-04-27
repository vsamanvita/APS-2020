#given a n,ith bit,the codelet returns 2^i if set else returns 0
#i=0 for least significant bit
def check_bit(n,i):
	if n&(1<<i):
		return n&(1<<i) 
	else:
		return 0

print(check_bit(14,3))
print(check_bit(14,0))