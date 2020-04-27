# prints numbers that divide the sum of the factorials of their digits in base 10 in range 1 to n

f=[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def sum_fact(n):
	global f
	v=[]
	for i in range(1,n+1):
	    sm=0
	    l=[int(i) for i in str(i)]
	    for j in l:
	        sm+=f[j]
	    if sm%i==0:
	        v.append(i)
	return(v)

n=1000
v=sum_fact(n)
print(v)