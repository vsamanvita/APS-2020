#calculate sum of huge numbers and prints the first 10 digits of the answer
import sys
n=int(sys.stdin.readline())
s=0
for _ in range(n):
    a=int(sys.stdin.readline())
    s+=a
s=str(s)
print(s[:10])