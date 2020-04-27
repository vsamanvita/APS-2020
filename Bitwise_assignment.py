#Consider u have
'''
Given x,a,b
1st if
if x==a:
	x=b
2nd if
if x==b:
	x=a
'''
#Can be replaced with XOR

#ex for 2nd if
a=5
b=3
x=3
x=a^b^x
print(x)

#ex for 1st if
a=5
b=3
x=5
x=a^b^x
print(x)