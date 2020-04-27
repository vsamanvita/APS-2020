### Juggler sequence
import math
def juggler(n):
    a=n
    print(a)
    while a!=1:
        if a%2==0:
            a=math.floor(math.sqrt(a))
        else:
            a=math.floor(math.sqrt(a)**3)
        print(a)
n=int(input())
juggler(n)