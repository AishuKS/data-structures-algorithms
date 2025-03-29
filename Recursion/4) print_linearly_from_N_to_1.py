def linearPrinting(num, N):
    if num>0:
        print(num)
        linearPrinting(num-1,N)

linearPrinting(10,10)