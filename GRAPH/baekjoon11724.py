from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
#print(n,m, num)
graph = [[] for i in range(n+1)]
#graph = []
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited_b = [False] * (n+1)


def bfs(graph, start, visited_b):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    result = []
    # 현재 노드를 방문 처리
    visited_b[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        #print(v, end=' ')
        result.append(v)
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:

            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True
    return result
#print(graph)

vv = []
flag =0
for i in range(1,n+1):
    if(i not in vv):
        vv += bfs(graph, i, visited_b)
        flag+=1




#print(vv)
print(flag)