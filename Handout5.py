#prints first n numbers whose sum of digits is equal to 10
TEN=10

def getSum(n):
	global TEN
	sm=0
	while n>0:
		sm+=n%TEN
		n=n//TEN
	return sm

def getn(n):
	sm=getSum(n)
	if sm%TEN==0:
		return n*TEN
	extra=TEN-(sm%TEN)
	return (n*TEN)+extra

n=10
for i in range(1,n+1):
	print(getn(i))
