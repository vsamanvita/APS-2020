#Sorting of a matrix based on nth column 
#column n E[0,n-1]
n=1 #nth column
a=[[51,28],[63,15],[13,13],[23,82],[43,51]]
a.sort(key=lambda l:l[n], reverse=True)
print(a)

#default 1st column
a.sort()
print(a)