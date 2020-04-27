# Program to find exponential value given base and exponent
def exponential(base,exp):
	t=1
	while exp>0:
		if exp%2!=0:
			t*=base
		base*=base
		exp=exp//2
	return t

base=76541
exp=243
print(exponential(base,exp))

