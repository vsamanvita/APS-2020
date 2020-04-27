#prints nth superfactorial i.e superfact is product of first n factorials.
#Ex: superfact(3)=1!*2!*3!
def superfact(n):
	fact=1
	b=1
	for i in range(n,0,-1):
		fact*=pow(b,i)
		b+=1
	return(fact)

print(superfact(4))
