import math
def getfact(n) : 
    c = 0
    d=[]
    for i in range(1,math.floor(math.sqrt(n))+1) : 
        if n%i == 0 :  
            if n/i == i : 
                d.append(i)
            else :
                d.append(i)
                d.append(int(n/i))
    return(sum(d)-n)

def amicable(a,b):
    return((getfact(a)==b) & (getfact(b)==a))

x=220
y=284
res=amicable(x,y)
if res:
    print("Amicable Pairs")
else:
    print("Non Amicable Pairs")