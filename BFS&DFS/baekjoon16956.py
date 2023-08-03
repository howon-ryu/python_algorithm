from collections import deque
import sys
input = sys.stdin.readline
r, c = map(int, sys.stdin.readline().split())

# 2차원 리스트의 맵 정보 입력 받는다.
graph = []
for _ in range(r):
    graph.append(list(map(str, input())))

# 좌/우/위/아래 방향 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[0]*c for _ in range(r)]

res = 1

def bfs(i,j):
    global res
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if(graph[nx][ny]=='S'):
                    res = 0

                elif(graph[nx][ny]!='D'):
                    q.append((nx,ny))
                    visited[nx][ny] = 1





for i in range(r):
    for j in range(c):
        if graph[i][j] == '.':
            graph[i][j] = "D"

for i in range(r):
    for j in range(c):
        if(graph[i][j] == 'W'):
            bfs(i,j)


print(res)
for i in graph:
    print(*i,sep='',end='')