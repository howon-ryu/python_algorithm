import sys
input = sys.stdin.readline
code = [0]
code += list(input().rstrip())
dp = [0]*(len(code)+1)
dp[0]=1
dp[1]=1
if code[1] == '0':
    print(0)
    exit(0)
for i in range(2,len(code)):
    if(int(code[i])>0):
        dp[i]+=dp[i-1]
    if(int(int(code[i-1])*10+int(code[i]))>=10 and int(int(code[i-1])*10+int(code[i]))<=26):
        dp[i] += dp[i-2]
print(dp[len(code)-1]%1000000)

