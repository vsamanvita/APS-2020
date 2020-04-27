#toggle the bit at given position
#LSB position is 0
def togglebit(n,bit):
	n^=(1<<bit)
	return(n)
n=15
print(togglebit(15,2))
print(togglebit(11,2))