#prints whether a given number is amstrong or not
#Armstrong num is a num with m digits whose sum of mth power of its digits is equal to the num itsself.
def armstrong(n):
	li=[int(i) for i in str(n)]
	exp=len(li)
	sm=0
	for i in li:
		sm+=pow(i,exp)
	if sm==n:
		return("Armstrong")
	else:
		return("Not armstrong")


print(armstrong(1634))