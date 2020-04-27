#if n is power of 2 divide it by 2,else subtract nearest power of 2 until n==1
#prints number of times the operation is it be done
def counterGame(n):
    count=0
    while(n>1):
        if n&(n-1):
            n-=2**math.floor(math.log(n,2))
        else:
            n>>=1
        count+=1
    print(count)

    if count&1:
        return('Louise')
    else:
        return('Richard')
