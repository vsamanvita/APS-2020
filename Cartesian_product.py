from itertools import product

#only with one list
arr=[1,2,3]
#repeat=2 i.e arr*,repeat=3 i.e arr*arr*arr
l=list(product(arr,repeat=3))

#different arrays
arr1=[1,2,3]
arr2=[2,3]
arr3=[3]
cartesian=list(product(arr1,arr2,arr3))
print(cartesian)