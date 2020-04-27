# Given a number n this codelets returns the count where n^x>n where xE(0,n)

def theGreatXor(n):
    count=0
    cur=-1
    pre=0
    while(n):
        a=n&1
        n>>=1
        cur+=1
        if a==1:
            count+=(pow(2,cur)-1)-(pow(2,pre+1)-1)
            pre=cur
            print(count,n)

    return(count+1)