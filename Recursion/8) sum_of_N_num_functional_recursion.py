def countNum(N):
    if N==0:
        return 0
    else:
        return N + countNum(N-1)

print(countNum(3))