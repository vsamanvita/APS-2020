def check_power(n):
	if n&(n-1)==0:
		print("Power of 2")
	else:
		print("Not power of 2")

n=128
check_power(n)