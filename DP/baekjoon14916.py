n = int(input())


dp = [0] *(100001)
dp[0] = 0
dp[1] = -1
dp[2] = 1
dp[3] = -1
dp[4] = 2
dp[5] = 1
dp[6] = 3
dp[7] = 2
dp[8] = 4

if(n >=8):
    for i in range(9,n+1):
        dp[i] = dp[i-5]+1

print(dp[n])

