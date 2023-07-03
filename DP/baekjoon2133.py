n = int(input())


dp = [0]*(31)
dp[1] = 0
dp[2] = 3
dp[3] = 0

for i in range(1,n+1):
    if (i>=4 and i%2==0):

        dp[i] = dp[i-2]*3+sum(dp[:i-2])*2+2
    elif(i ==2 ):
        dp[i] = 3
    else:
        dp[i] = 0
    if(i == n):
        print(dp[n])

