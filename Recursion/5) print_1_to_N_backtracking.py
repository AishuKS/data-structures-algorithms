def backtrackPrinting(num, N):
    if num < 1:
        return
    backtrackPrinting(num-1,N)
    print(num)

backtrackPrinting(10,10)