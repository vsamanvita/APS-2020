def check_bit(n,i):
	res=n&(1<<i)
	print(res)

#unset ith bit in a given number
def unsetbit(n,i):
	#bit before unset
	check_bit(n,i)
	n=n & ~(1<<i)
	#bit after unset
	check_bit(n,i)


unsetbit(15,3)



