# cook your dish here
import math
priority={'+':1, '-':1, '*':2, '/':2, '^':3}
from fractions import Fraction as frac
# out=[]
# arr=[]
def great(i):
	try:
		a=priority[i]
		b=priority[arr[len(arr)-1]]
		return True if a  <= b else False
	except:
		return False

def infixtopost(exp,out,arr):
	for i in exp:
		if i.isalpha():
			out.append(i)
		elif i=="(":
			arr.append(i)
		elif i==")":
			while(len(arr)>0 and arr[len(arr)-1]!="("):
				# print(arr)
				data=arr.pop()
				out.append(data)
			if len(arr)>0 and arr[len(arr)-1]=="(":
				arr.pop()
		else:
			while(len(arr)>0 and great(i)):
				out.append(arr.pop())
			arr.append(i)
		# print(arr)
		# print(out)
		# print("----------")
	while len(arr)>0:
		data=arr.pop()
		out.append(data)
	return("".join(out))

exp="a+b*(c^d-e)^(f+g*h)-i"
out=[]
arr=[]
pre=infixtopost(exp,out,arr)
print(pre)