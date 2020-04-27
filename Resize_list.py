# Program to resize a list into specified size.

from math import ceil

def resize(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))

print(resize([1,2,3,4,5,6,7,8,9],3))