#Converts the given string to lowercase
#Method1
def upper_lower(s):
	res=[]
	for i in s:
		i=chr(ord(i)|32)
		res.append(i)
	return "".join(res)
	
s="ABcDE"
r=upper_lower(s)
print(r)

#Method 2
print(s.lower())
