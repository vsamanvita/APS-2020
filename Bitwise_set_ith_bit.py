def check_bit(n,i):
	res=n&(1<<i)
	print(res)

#set ith bit in a given number
def setbit(n,i):
	#bit before set
	check_bit(n,i)
	n=n|(1<<i)
	#bit after set
	check_bit(n,i)

setbit(14,0)