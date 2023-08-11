import sys
input = sys.stdin.readline



n,s,r = map(int,input().split())
damage = list(map(int,input().split()))
extra = list(map(int,input().split()))


boat = [1]*(n+2)
for i in damage:
    boat[i] = 0
for i in extra:
    boat[i]+=1



for i in range(1,n+1):
    if(boat[i]==2):
        if(boat[i-1]==0):
            boat[i]-=1
            boat[i - 1]+=1
        elif(boat[i+1]==0):
            boat[i] -= 1
            boat[i + 1] += 1

cnt=0
for i in boat:
    if(i==0):
        cnt+=1
print(cnt)