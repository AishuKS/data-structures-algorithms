nums = [2,3,7,8,10]
n = len(nums)
target = 11

dp = [[0] * (target+1) for i in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(1,n+1):
    for j in range(1, target+1):
        if j >= nums[i-1]:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        else:
            dp[i][j] = dp[i-1][j]

for i in range(n+1):
    print(dp[i])