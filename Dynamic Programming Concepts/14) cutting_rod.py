"""
Given a rod of length n inches and an array price[], where price[i] denotes the value of a piece of length i. 
Your task is to determine the maximum value obtainable by cutting up the rod and selling the pieces.
Note: n = size of price, and price[] is 1-indexed array.

Example:

Input: price[] = [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation: The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5 + 17 = 22.

Input: price[] = [3, 5, 8, 9, 10, 17, 17, 20]
Output: 24
Explanation: The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1] = 8*3 = 24.

Input: price[] = [3]
Output: 3
Explanation: There is only 1 way to pick a piece of length 1.
"""

def cutRod(price):
    n = len(price)
    dp = [0] * (n+1)
    for i in range(1,n+1):
        for j in range(i):
            dp[i] = max(dp[i], dp[i-j-1]+price[j])

    return dp[n]

price = [2,5,7,8]
print(cutRod(price))
