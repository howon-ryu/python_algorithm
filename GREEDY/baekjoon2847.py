import sys

input = sys.stdin.readline


n = int(input())

level = []
cnt=0
for _ in range(n):
    level.append(int(input()))


for i in range(n-1,0,-1):
    if(level[i]<=level[i-1]):
        while (level[i]<=level[i-1]):

            level[i - 1]=level[i - 1]-1
            cnt+=1



print(cnt)

