n = 4
W = 8
weights = [3,4,6,5]
prices = [2,3,1,4]
dp = [[0]*(W+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(W+1):
        if weights[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], prices[i-1]+dp[i-1][j-weights[i-1]])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][W])