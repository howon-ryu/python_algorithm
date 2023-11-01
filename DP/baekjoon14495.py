import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for i in range(n+1)]
if(n<=3):
    dp.append(0)
    dp.append(0)
    dp.append(0)
    dp.append(0)
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4,n+1):
    dp[i] = dp[i-1]+dp[i-3]





print(dp[n])