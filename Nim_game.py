#Nim game.
#Alice starts the game.
#Alice and Bob play alternatively.

def nim(a):
	n=len(a)
	res=0
	for x in range(n):
		res^=a[x]

	if res==0 or n%2==0:
		return "Alice" 
	else:
		return "Bob"
		