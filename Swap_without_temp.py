#Given 2 numbers a,b,the codelet swaps the 2 numbers.

#Method1:bitwise(XOR)
def swap_num(a,b):
	a=a^b
	b=a^b
	a=a^b
	print("After swap")
	print("a:",a,"b:",b)

#Method2
def swap_num1(a,b):
	a=a+b
	b=a-b
	a=a-b
	print("After swap")
	print("a:",a,"b:",b)

print("a:",10,"b:",15)
swap_num(10,15)
swap_num1(10,15)