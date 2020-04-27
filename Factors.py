#All the factors of a number
#eg:if n=10 factors=[1,2,5,10] no_of_factors=4
import math
def getfact(n) : 
    c = 0
    d=[]
    for i in range(1,math.floor(math.sqrt(n))+1) : 
        if n%i==0 :  
            if n/i==i : 
                d.append(i)
            else :
                d.append(i)
                d.append(int(n/i))
    return(d)
n=20
res=getfact(n)
print(len(res))
print(res)