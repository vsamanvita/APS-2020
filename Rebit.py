# cook your dish here
import math
from fractions import Fraction as frac
# Python program to convert infix expression to postfix 
# Class to convert the expression 
class Conversion: 
	
	# Constructor to initialize the class variables 
	def __init__(self, capacity): 
		self.top = -1
		self.capacity = capacity 
		# This array is used a stack 
		self.array = [] 
		# Precedence setting 
		self.output = [] 
		self.precedence = {'|':1,'^':2,'&':3} 
	
	# check if the stack is empty 
	def isEmpty(self): 
		return True if self.top == -1 else False
	
	# Return the value of the top of the stack 
	def peek(self): 
		return self.array[-1] 
	
	# Pop the element from the stack 
	def pop(self): 
		if not self.isEmpty(): 
			self.top -= 1
			return self.array.pop() 
		else:
			return "$"
	
	# Push the element to the stack 
	def push(self, op): 
		self.top += 1
		self.array.append(op) 

	# A utility function to check is the given character 
	# is operand 
	def isOperand(self, ch): 
		return ch=='#'

	# Check if the precedence of operator is strictly 
	# less than top of stack or not 
	def notGreater(self, i): 
		try: 
			a = self.precedence[i] 
			b = self.precedence[self.peek()] 
			return True if a <= b else False
		except KeyError: 
			return False
			
	# The main function that converts given infix expression 
	# to postfix expression 
	def infixToPostfix(self, exp): 
		
		# Iterate over the expression for conversion 
		for i in exp: 
			# If the character is an operand, 
			# add it to output 
			if self.isOperand(i): 
				self.output.append(i) 
			
			# If the character is an '(', push it to stack 
			elif i == '(': 
				self.push(i) 

			# If the scanned character is an ')', pop and 
			# output from the stack until and '(' is found 
			elif i == ')': 
				while( (not self.isEmpty()) and self.peek() != '('): 
					a = self.pop() 
					self.output.append(a) 
				if (not self.isEmpty() and self.peek() != '('): 
					return -1
				else: 
					self.pop() 

			# An operator is encountered 
			else: 
				while(not self.isEmpty() and self.notGreater(i)): 
					self.output.append(self.pop()) 
				self.push(i)

		# pop all the operator from the stack 
		while not self.isEmpty(): 
			self.output.append(self.pop())
        
		return "".join(self.output)
		
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

t=int(input())
for _ in range(t):
    l=input()
    if len(l)==1:
        print('748683265 748683265 748683265 748683265')
    else:
        obj = Conversion(len(l)) 
        eq=obj.infixToPostfix(l)
        # print(eq)
        
        st=[]
        for x in eq:
            if x=='#':
                st.append(x)
            else:
                q1=st.pop()
                q2=st.pop()
                
                count=0
                if type(q1)==list:
                    count+=math.log(sum(q1),4)
                if  type(q2)==list:
                    count+=math.log(sum(q2),4)
                
                if not (type(q1)==list and type(q2)==list):
                    count+=1
                    count=int(count)
                    
                if x=='&':
                    if q1=='#' and q2=='#':
                        ans=[1,3,3,9]
                    elif q1=='#'and type(q2)==list:
                        b=int(2*math.sqrt(q2[0]))
                        c=int(pow(4,count)-q2[0])
                        xx=frac((int(-b+math.sqrt(b**2+4*c))),2)
                        # print('qqqqqq',b,c,xx)
                        ans=[q2[0],int(math.sqrt(q2[0]))*xx,int(math.sqrt(q2[0]))*xx,xx**2]
                    elif q2=='#'and type(q1)==list:
                        b=2*math.sqrt(q1[0])
                        c=pow(4,count)-q1[0]
                        xx=frac((int(-b+math.sqrt(b**2+4*c))),2)
                        # print('qqqqqq',b,c,xx)
                        ans=[q1[0],int(math.sqrt(q1[0]))*xx,int(math.sqrt(q1[0]))*xx,xx**2]
                    else:
                        b=2*math.sqrt(q2[0]*q1[0])
                        c=pow(4,count)-(q2[0]*q1[0])
                        xx=frac((int(-b+math.sqrt(b**2+4*c))),2)
                        ans=[q2[0]*q1[0],int(math.sqrt(q2[0]*q1[0]))*xx,int(math.sqrt(q2[0]*q1[0]))*xx,xx**2]
                
                
                elif x=='|':
                    if q1=='#' and q2=='#':
                        ans=[9,3,3,1]
                    elif q1=='#'and type(q2)==list:
                        b=int(2*math.sqrt(q2[3]))
                        c=int(pow(4,count)-q2[3])
                        xx=frac((int(-b+math.sqrt(b**2+4*c))),2)
                        ans=[xx**2,int(math.sqrt(q2[3]))*xx,int(math.sqrt(q2[3]))*xx,q2[3]]
                    elif q2=='#'and type(q1)==list:
                        b=2*math.sqrt(q1[3])
                        c=pow(4,count)-q1[3]
                        xx=frac((int(-b+math.sqrt(b**2+4*c))),2)
                        ans=[xx**2,int(math.sqrt(q1[3]))*xx,int(math.sqrt(q1[3]))*xx,q1[3]]
                    else:
                        b=int(2*math.sqrt(q2[3]*q1[3]))
                        c=int(pow(4,count)-(q2[3]*q1[3]))
                        xx=frac((int(-b+math.sqrt(b**2+4*c))),2)
                        ans=[xx**2,int(math.sqrt(q2[3]*q1[3]))*xx,int(math.sqrt(q2[3]*q1[3]))*xx,q2[3]*q1[3]]
                        
                        
                else:
                    if q1=='#' and q2=='#':
                        ans=[4,4,4,4]
                    elif type(q1)==list and type(q2)==list:
                        zz=q1[0]*q2[0]+q1[1]*q2[1]+q1[2]*q2[2]+q1[3]*q2[3]
                        b=int(2*math.sqrt(zz))
                        c=int(pow(4,count)-(zz))
                        xx=frac((int(-b+math.sqrt(b**2+4*c))),2)
                        ans=[xx**2,int(math.sqrt(zz))*xx,int(math.sqrt(zz))*xx,zz]
                    else:
                        z=pow(4,count-1)
                        ans=[z,z,z,z]
                # print(ans)
                # print(count,ans)
                st.append(ans)
                
        # print(st)
        sol=[]
        m = 998244353
        for it in st[0]:
            num=frac(it).numerator
            den=int(sum(st[0]))*frac(it).denominator
            # print(num,den)
            sol.append(num*pow(den,m-2,m)%m)
            
        print(sol[3],sol[0],sol[1],sol[1])
# 4
# (#&#|#)|(#|#^#)
# (#&#|#)^(#|#^#)
# (#&#|#)&(#|#^#)
# (#&#|#)|(#|#^#)&(#&#|#)&(#|#^#)^(#|#^#)&(#&#|#)&#|#|(#|#^#)&(#&#|#)&(#|#^#)^(#|#^#)
# ##&#|###^||
# [[3364.0, 348.0, 348.0, 36]]
# 989470721 178397185 913432577 913432577
# ##&#|###^|^
# [[784.0, 1008.0, 1008.0, 1296.0]]
# 682393601 807174145 752582657 752582657
# ##&#|###^|&
# [[900.0, 1020.0, 1020.0, 1156.0]]
# 716513281 778903553 749658113 749658113
# ##&#|###^|##&#|&###^|&###^|##&#|&#&^|#|###^|##&#|&###^|&###^|^|
# [[1.6781198727983989e+19, 8.130752890131579e+17, 8.130752890131579e+17, 3.93947676992471e+16]]
# 31561309 123824033 421429506 421429506