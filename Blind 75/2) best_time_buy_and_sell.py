import sys

def maxProfit(array):
    minNum = sys.maxsize
    maxNum = 0
    for i in array:
        minNum = min(minNum, i)
        maxNum = max(maxNum, i-minNum)
    return maxNum

input = [7,1,5,3,6,4]
print(maxProfit(input))