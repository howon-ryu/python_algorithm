n = int(input())

for i in range(n):
    num = int(input())
    if(num == 1):
        print(1)
    elif(num == 2):
        print(1)
    elif (num == 3):
        print(1)
    elif (num == 4):
        print(2)
    elif (num == 5):
        print(2)
    else:
        dp = [0]*(num+1)

        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
        for j in range(6,num+1):
            dp[j] = dp[j-1]+dp[j-5]
        print(dp[num])
