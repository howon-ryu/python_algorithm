import sys
import copy
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    o = 0
    v = 0

    while q:
        x, y = q.popleft()

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    continue
                elif graph[nx][ny] == 1:
                    v += 1

                q.append((nx, ny))
                visited[nx][ny] = 1

    return 1



t = int(input())
a = 0
for _ in range(t):
    m,n,k = map(int, input().split())




    visited = [[0 for _ in range(m)] for _ in range(n)]
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        # graph.append(list(map(int,input().split())))
        t_a,t_b = map(int, input().split())

        graph[t_b][t_a] = 1

    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    #print(visited)
    #print(graph)
    for i in range(n):
        for j in range(m):
            if graph[i][j] ==1 and visited[i][j] ==0:
                a+=bfs(i,j)
    print(a)
    a = 0




