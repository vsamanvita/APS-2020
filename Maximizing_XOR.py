# Maximum xor between any 2 numbers in the range [l,r]

def maximizingXor(l, r):
    return l^r|2**math.ceil(math.log(l^r,2))-1