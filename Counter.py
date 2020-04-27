#Counter takes a iterable and counts the number of occurances where iterable is the key and occurances is value
from collections import Counter
a=[22,43,55,55,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,4,5,5,7,38,38,38,63]
d=Counter(a)
d=d.most_common()
#max occurance 
print(d[0][1])
#key repeating most number of times
e=dict(d)
key=list(e.keys())
val=list(e.values())
for i in range(len(val)):
    if val[i]==d[0][1]:
        print(key[i],end=" ")