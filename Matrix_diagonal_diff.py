def diagonalDifference(arr):
    n=len(arr)
    a=0
    b=0
    for i in range(len(arr[1])):
        for j in range(len(arr[1])):
            if i==j:
                a=a+arr[i][j]
    for i in range(len(arr[1])):
        for j in range(len(arr[1])):
            if (i+j)==(n-1):
                b=b+arr[i][j]
    d=abs(a-b)
    # print(a,b)
    return(d)

a=[[11,2,4],[4,5,6],[10,8,-12]]
res=diagonalDifference(a)
print(res)
