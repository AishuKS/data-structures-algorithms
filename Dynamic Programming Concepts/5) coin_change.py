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