def linearPrint(num, N):
    if num<=N:
        print(num)
        linearPrint(num+1, N)

linearPrint(1,10)