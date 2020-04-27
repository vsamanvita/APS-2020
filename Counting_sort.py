# input array and max element.

def countingSort(arr,maxx):
    res=[0 for x in range(maxx+1)]

    for x in arr:
        res[x]+=1

    result=[]
    for x in range(maxx+1):
        while res[x]:
            result.append(x)
            res[x]-=1
    return result