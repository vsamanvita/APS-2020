# program to find the unique element in the array 

def lonelyinteger(a):
    lone=0
    for x in a:
        lone^=x
    return lone