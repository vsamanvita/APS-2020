#lookup table to store bits set to 1 in the number
n=int(input())
a=[int(i) for i in input().split()]
look=[0]
for i in range(1,256*256):
    look.append((i&1)+look[i//2])
    
#query to find sum of bits set for all numbers in a array
s=0
for i in a:
    s+=look[i & 0xffff]+look[(i>>16) & 0xffff]
print(s)