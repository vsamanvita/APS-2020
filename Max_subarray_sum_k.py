def maxk(arr,X):
    c=arr[0]
    sm=0
    s=0
    for i in range(1,len(arr)):
        if c<=X:
            sm=max(sm,c)
        while c+arr[i]>X and s<i:
            c-=arr[s]
            s+=1
        c+=arr[i]
    if c<=X:
        sm=max(sm,c)
    return(sm)

arr=[6,7,8,9,10]
print(maxk(arr,16))