#prints all squared palindromes in a gien range
#Sq palindrome is a number which is a palindrome and its sqroot is also a palindrome
import math

def palindrome(s):    
    s=str(s)
    flag=0
    sr=s[::-1]
    for i in range(len(s)):
        if s[i]!=sr[i]:
            flag=1
            break
    if flag==1:
        return False
    return True
    


def squared_palindrome(l,r):
    res=[]
    for i in range(l,r+1):
        ls=i
        lsq=math.sqrt(i)
        if lsq.is_integer():
            lsq=int(lsq)
            if palindrome(ls) and palindrome(lsq):
                res.append(i)
    return(res)


l=1
r=10000
res=squared_palindrome(l,r)
print(res)