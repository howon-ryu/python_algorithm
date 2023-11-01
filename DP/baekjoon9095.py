import sys

input = sys.stdin.readline

n = int(input())
arr =[]
for i in range(n):
    a = int(input())
    arr.append(a)

dp = [0 for i in range(11)]
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
if(max(arr)>4):
    for i in range(4,max(arr)+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

#print(dp)
for i in arr:
    print(dp[i])

