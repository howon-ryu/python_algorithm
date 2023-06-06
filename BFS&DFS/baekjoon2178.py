from collections import deque

n,m = map(int,input().split())
miro = []

for _ in range(n):
  miro.append(list(map(int, input())))


def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    # 현재 노드를 방문 처리

    # 큐가 빌 때까지 반복
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx<0 or nx>=n or ny<0 or ny>=m):
                continue
            if(miro[nx][ny]==0):
                continue
            if(miro[nx][ny] ==1):
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
    return miro[n-1][m-1]

print(bfs(0,0))



