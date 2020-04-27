#converts the given string to uppercase
#Method 1

def lower_upper(s):
	res=[]
	for i in s:
		i=chr(ord(i)&~32)
		res.append(i)
	return "".join(res)

s="abCde"
r=lower_upper(s)
print(r)

# Method 2
print(s.upper())