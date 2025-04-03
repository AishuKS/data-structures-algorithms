def powerOfTwo(n):
    return n>0 and (n & (n-1)) == 0

n = 16
print(powerOfTwo(n))