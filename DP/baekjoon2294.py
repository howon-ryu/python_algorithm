n,k = map(int,input().split())


def coindp(array):
    dp = [100001]*(k+1)
    dp[0]=0

    for i in coin_list:
        for j in range(i,k+1):
            if(dp[j]>0):
                dp[j] = min(dp[j-i]+1,dp[j])
    if(dp[k] == 100001):
        print (-1)
    else:
        print(dp[k])




coin_list = []

for i in range(n):
    coin = int(input())
    coin_list.append(coin)



coindp(coin_list)