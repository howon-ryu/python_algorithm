import sys

from collections import deque
import copy
n, m = map(int, sys.stdin.readline().split())

tomato = []
for i in range(m):
     tomato.append(list(map(int, sys.stdin.readline().split())))


def bfs():





        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while queue:
            x,y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(nx<0 or nx>=m or ny<0 or ny>=n):
                    continue

                if(tomato[nx][ny]==-1):
                    continue
                if(tomato[nx][ny] == 0):

                    tomato[nx][ny] =tomato[x][y]+1
                    queue.append((nx, ny))




queue = deque()

res = 0

for i in range(m):
    for j in range(n):
        if(tomato[i][j]==1):

            queue.append([i, j])



bfs()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)





