import sys

from collections import deque
input = sys.stdin.readline
def bfs(graph, start):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited = [False] * (n + 1)
    temp = 0
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        temp+=1
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:

            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return temp


n,m = map(int,input().split())
#print(n,m, num)
graph = [[] for i in range(n+1)]
#graph = []
for i in range(m):
    a,b = map(int,input().split())

    graph[b].append(a)

    graph[b].sort()

# print(graph)

tt = []
maxCnt = 1

# 정의된 BFS 함수 호출
for i in range(1,n+1):

    cnt = bfs(graph, i)
    if(cnt>maxCnt):
        maxCnt = cnt
        tt.clear()
        tt.append(i)
    elif cnt == maxCnt:
        tt.append(i)




print(*tt)