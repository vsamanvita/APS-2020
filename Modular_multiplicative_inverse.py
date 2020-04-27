#given a,b such that (a>=0,b>0) and b is co prime with m
#computes (a*b^-1)%m i.e modular multiplicative inverse
a=9
b=16
m=998244353 
res=a*pow(b,m-2,m)%m
print(res)