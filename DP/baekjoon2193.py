import sys
input = sys.stdin.readline


n = int(input())
dp=[]
if(n==1):
    print(1)
    exit(0)
elif(n==2):
    print(1)
    exit(0)
else:
    dp = [0]*(n+1)
    dp[1]=1
    dp[2]=1


for i in range(3,n+1):
    dp[i] = dp[i-2]+dp[i-1]


print(dp[n])