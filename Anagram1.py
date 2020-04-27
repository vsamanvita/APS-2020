#Given a string s divide tthe string into 2 parts
#returns minimum number of changes required to make them anagrams
#returns -1 if cannot be formed
from collections import defaultdict,Counter
def anagram(s):
    c=0
    if len(s)%2==1:
        return("-1")
    a=len(s)//2
    # print(a)
    s=list(s)
    s1=s[:a]
    # print(s1)
    s2=s[a:]
    d=dict(Counter(s2))
    d=defaultdict(str,d)
    # print(d)
    for i in range(a):
        if s1[i] not in d or d[s1[i]]==0:
            c+=1
        else:
            d[s1[i]]-=1
    return(c)
print(anagram("aaabbb"))