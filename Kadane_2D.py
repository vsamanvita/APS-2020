#prints max subarray sum along with its matrix left,rigth,top and bottom indexes.
#2D kadane
def kadane(a):
    maxx=float("-inf")
    tmax=0
    st=-1
    for x in range(n):
        tmax+=a[x]
        if maxx<tmax:
            maxx=tmax
            end=x
            start=st+1
        if tmax<0:
            tmax=0
            st=x
    return(maxx,start,end)
  
def kadane_2d(a,n):
    maxsum=float("-inf")
    maxleft=0
    maxright=0
    top=0
    bottom=0
    for left in range(n):
        temp=[0]*m
        for right in range(left,n):
            temp=[sum(i) for i in zip(temp,a[right])]
            # print(temp,left,right)
            cursum,up,down=kadane(temp)
            if cursum>maxsum:
                maxsum=cursum
                top=up
                bottom=down
                maxleft=left
                maxright=right
    return(maxsum,maxleft,maxright,top,bottom)
            
n,m=map(int,input().split())
a=[]
for i in range(n):
    b=[int(i) for i in input().split()] 
    a.append(b)
maxsum,maxleft,maxright,top,bottom=kadane_2d(a,n)
print("Max subarray sum of 2d matrix is ",maxsum)
print("Left index:",maxleft,"Rigth index:",maxright,"Top index:",top,"Bottom index:",bottom)