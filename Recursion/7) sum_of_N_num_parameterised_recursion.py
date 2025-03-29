def countNum(num,N, total=0):
    if num<=N:
        total = total + num
        countNum(num+1, N, total)
    else:
        print(total)
    
countNum(1,10)