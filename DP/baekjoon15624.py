import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())

dp = [0]*(n+2)

dp[1] = 1
for i in range(2,n+1):
    dp[i] = (dp[i-1]+dp[i-2])%1000000007


print(dp[n])


