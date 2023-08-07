import sys

input = sys.stdin.readline


h,w = map(int,input().split())
rain = list(map(int,input().split()))

world = [[0 for _ in range(w)] for _ in range(h)]

def wall_find(x,y):

    if(y!=0 and y!=(w-1)):
        leftwall=0
        rightwall = 0

        for j in range(y):

            if(world[x][j]==1):
                leftwall=1




        for k in range(y,w):


            if (world[x][k] == 1):
                rightwall = 1
        if(leftwall==1 and rightwall==1):
            # print(x,y)
            return 1
        else:
            return 0
    else:
        return 0

cnt=0
for i in range(h):
    for j in range(w):

        if(world[i][j]==0 and i<rain[j]):
            world[i][j] =1

for i in range(h):
    for j in range(w):
        if(world[i][j]==0):

            res=wall_find(i,j)
            if(res==1):
                cnt+=1

print(cnt)
# print(world)
