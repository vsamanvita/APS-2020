#Absolute differnce between 1^2+2^2+...+n^2 and (1+2+...+n)^2
import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sumsq=n*(2*n+1)*(n+1)/6
    # print(sumsq)
    sm=n*(n+1)/2
    print(int(abs(sumsq-sm*sm)))
