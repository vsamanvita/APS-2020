# Given a list of Gigantic numbers in strings. This codelet returns the sorted list.

def bigSorting(a):
    a.sort()
    a.sort(key=len)
    return(a)
