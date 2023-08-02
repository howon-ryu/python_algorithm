import sys
input = sys.stdin.readline


n = int(input())
p_list = list(map(int,input().split()))


q = int(input())

dp = [[0]*n for _ in range(n)]

for num_len in range(n):
    for start in range(n-num_len):
        end = start+num_len

        if (start ==end):
            dp[start][end] =1
        elif p_list[start] == p_list[end]:
            if ((start+1) == end):
                dp[start][end] = 1
            elif (dp[start+1][end-1]==1):
                dp[start][end] =1
for _ in range(q):
    s,e = map(int,input().split())
    print(dp[s-1][e-1])

