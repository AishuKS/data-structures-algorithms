"""
You are given an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be 
made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
"""

coins = [1,2,5]
amount = 10

n = len(coins)
INF = amount + 1
dp = [[INF] * (amount+1) for i in range(n+1)]

for i in range(n+1):
    dp[i][0] = 0

for i in range(1, n+1):
    for j in range(1, amount+1):
        if j>=coins[i-1]:
            value = dp[i][j-coins[i-1]]+1
            dp[i][j] = min(value, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

if dp[n][amount] != INF:
    print(dp[n][amount])
else:
    print(-1)