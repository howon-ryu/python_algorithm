r,c = map(int, input().split())

dp = [[1]*i for i in range(1,32)]

for i in range(2,31):
    for j in range(1,len(dp[i])-1):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
print(dp[r-1][c-1])