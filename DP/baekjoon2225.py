n,k = map(int,input().split())

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]



for j in range(1,n+1):
    for i in range(1,k+1):
        if(i == 1):
            dp[i][j] = 1
        elif(j==1):

            dp[i][j] = i
        else:
            dp[i][j] = dp[i][j-1]+dp[i-1][j]

        if(j == n and i ==k):
            print(dp[i][j]%1000000000)