import sys
input = sys.stdin.readline



n,k = map(int, input().split())

coin = []

for _ in range(n):
    coin.append(int(input()))




max_cnt = 0
for i in range(len(coin)):
    if(k<coin[i]):
        max_cnt=i-1
        break

    elif(k==coin[i]):
        max_cnt=i
        break
    elif(k>coin[i]):
        if(i == (len(coin)-1)):
            max_cnt=i
# print(max_cnt)
cnt = 0
while k>0:
    cnt += k//coin[max_cnt]
    k = k%coin[max_cnt]
    max_cnt-=1


print(cnt)
