#Given 2 strings s1,s2 returns number of minimum deletions required to form anagrams.
from collections import Counter

def makingAnagrams(s1, s2):
    count=0
    di1=dict(Counter(s1))
    di2=dict(Counter(s2))
    a=set(s1).intersection(s2)
    a=list(a)
    for i in a:
        count+=min(di1[i],di2[i])
    return(len(s1)+len(s2)-2*count)

s1="abc"
s2="cca"
print(makingAnagrams(s1, s2))


