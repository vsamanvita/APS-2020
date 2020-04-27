#kadane algorithm 
#to print maximum subarray sum along with starting,ending indices and the array
def kadane(a,n):
    mx=float("-inf")
    suma=0
    ca=0
    for i in range(len(a)):
        suma+=a[i]
        if suma>mx:
            mx=suma
            bs=ca
            be=i
        if suma<0:
            suma=0
            ca=i+1
    res=[mx,bs,be]
    return(res)

n=int(input())
a=[int(i) for i in input().split()] 
res=kadane(a,n)
print("Max subarray sum is ",res[0])
print("Starting index is ",res[1])
print("Ending index is ",res[2])
print("Subarray is ",a[res[1]:res[2]+1])