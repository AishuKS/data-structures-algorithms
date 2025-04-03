'''
Given a number n and a bit number k, check if the kth index bit of n is set or not. A bit is called set if it is 1. 
The position of set bit '1' should be indexed starting with 0 from the LSB side in the binary representation of the number.
'''

def checkBit(n,k):
    return (n<<k) & 1 == 1

n = 4
k = 0
print(checkBit(n,k))