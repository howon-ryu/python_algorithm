from collections import deque
import sys
input = sys.stdin.readline
m_dx = [0,1,0,-1]
m_dy = [1,0,-1,0]
h_dx = [-2,-1,1,2,2,1,-1,-2]
h_dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(n):
    q = deque()
    q.append((0,0,n))
    count = [[[0]*(n+1)for _ in range(M)]for _ in range(N)]
    while q:
        x,y,K = q.popleft()
        if x == N-1 and y == M-1:
            return count[x][y][K]
        if K>0:
            for k in range(8):
                nx = x+h_dx[k]
                ny = y + h_dy[k]
                if 0<=nx<N and 0<=ny<M:
                    if road[nx][ny] != 1 and count[nx][ny][K-1]==0:
                        count[nx][ny][K-1] =count[x][y][K]+1
                        q.append((nx,ny,K-1))
        for k in range(4):
            nx = x+m_dx[k]
            ny = y + m_dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if road[nx][ny] != 1 and count[nx][ny][K] == 0:
                    count[nx][ny][K] = count[x][y][K] + 1
                    q.append((nx, ny, K))
    return -1
K  = int(input())
M,N = map(int,input().split())
road = []
for _ in range(N):
    road.append(list(map(int,input().split())))
result = bfs(K)
print(result)
