#Given 2 numbers x and y find min(x,y) and max(x,y) using bitwise
x=20
y=100
minv=(y^(x^y) & -(x<y))
maxv=(x^(x^y) & -(x<y))
print(maxv)
print(minv)