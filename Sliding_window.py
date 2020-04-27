#Prints maximum sum of a subarray of size k 
#if subarray of k cant be formed prints -1
import sys 
INT_MIN =float("-inf")
  
def maxSum(arr, n, k): 
    if not n>k:
        return -1
    max_sum=INT_MIN 
    w_sum=sum(arr[:k])  
    for i in range(n-k): 
        w_sum=w_sum-arr[i]+arr[i+k] 
        max_sum=max(w_sum,max_sum) 
    return max_sum 
  
arr=[1,0,2,9,3,5,4,8] 
k=4
n=len(arr)
print(maxSum(arr,n,k))