import sys
input = sys.stdin.readline

n = int(input())
num = int(input())

ascar = [[0]*(n) for _ in range(n)]
res = []
def up(n,m):
    ascar[n-1][m]=ascar[n][m]+1
    if(ascar[n-1][m]==num):
        res.append([n,m+1])
def right(n,m):
    ascar[n][m+1] = ascar[n][m] + 1
    if (ascar[n][m+1] == num):
        res.append([n+1, m+2])
def down(n,m):

    ascar[n+1][m] = ascar[n][m] + 1
    if (ascar[n+1][m] == num):
        res.append([n+2, m+1])
def left(n,m):
    ascar[n][m-1] = ascar[n][m] + 1
    if (ascar[n][m-1] == num):
        res.append([n+1, m])


x = n//2
y = n//2
ascar[x][y] = 1
for i in range(n):
    if(i%2==1):
        for _ in range(i):
            up(x,y)
            x-=1
        for _ in range(i):
            right(x,y)
            y+=1
        for _ in range(i+1):
            down(x,y)
            x+=1
        for _ in range(i+1):
            left(x,y)
            y-=1

for _ in range(n-1):
    up(x,y)
    x -= 1


for i in ascar:
    print(*i)

if(num==1):

    print(n//2+1,n//2+1)
else:
    print(*res[0])







