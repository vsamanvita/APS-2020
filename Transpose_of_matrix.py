#Find transpose of a matrix

#Method 1
a=[[1,2,3],[4,5,6],[7,8,9]]
transpose=[list(i) for i in zip(*a)]
print(transpose)

#Method 2
a=[[1,2],[4,5],[7,8]]
b=[[0 for i in range(len(a))]for i in range(len(a[0]))]
def transpose(a,b): 
    for i in range(len(a[0])): 
        for j in range(len(a)): 
            b[i][j]=a[j][i] 

transpose(a,b)
print(b)