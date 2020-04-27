#Check whether a number is perfect or abundant
import math
def getSum(n) : 
    c = 0
    sm=0
    for i in range(1,math.floor(math.sqrt(n))+1) : 
        if n%i == 0 :  
            if n/i == i : 
                sm+=i
            else :
                sm+=i
                sm+=int(n/i)
    return(sm)
n=int(input())
res=getSum(n)
res=res-n
if res==n:
    print("Perfect Number")
elif res>n:
    print("Abundant Number")
else:
    print("Neither")