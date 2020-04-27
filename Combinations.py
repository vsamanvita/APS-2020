#Generates all combinations ie rE[1,n]
from itertools import combinations

s="abcd"
for i in range(1,len(s)+1):
	for c in combinations(s,i):
		print("".join(c))
