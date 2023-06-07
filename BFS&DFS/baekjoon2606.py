from collections import deque

n = int(input())
m = int(input())
# n,m, num = map(int,input().split())
graph = [[] for i in range(n+1)]
#graph = []
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited_b = [False] * (n+1)
print(graph)
#
# def bfs(x, y):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     queue = deque()
#     queue.append((x,y))
#     # 현재 노드를 방문 처리
#
#     # 큐가 빌 때까지 반복
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if(nx<0 or nx>=n or ny<0 or ny>=m):
#                 continue
#             if(miro[nx][ny]==0):
#                 continue
#             if(miro[nx][ny] ==1):
#                 miro[nx][ny] = miro[x][y] + 1
#                 queue.append((nx, ny))
#     return miro[n-1][m-1]


def bfs(graph, start, visited_b):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    count = 0
    # 현재 노드를 방문 처리
    visited_b[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        # print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:

            if not visited_b[i]:
                queue.append(i)
                count +=1
                visited_b[i] = True
    return count
print(bfs(graph,1,visited_b))
# print(bfs(0,0))