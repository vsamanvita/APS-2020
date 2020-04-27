#Given a number n and number of bits b to be flipped returns the flipped value
def flippingBits(n,b):
    n^=(1<<b)-1
    return n

print(flippingBits(15,3))
print(1<<3)