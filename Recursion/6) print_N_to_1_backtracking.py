def backtrackPrint(num,N):
    if num>N:
        return
    backtrackPrint(num+1,N)
    print(num)
    
backtrackPrint(1,10)