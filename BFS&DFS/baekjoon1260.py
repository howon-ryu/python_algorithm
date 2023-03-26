from collections import deque







n,m, num = map(int,input().split())
#print(n,m, num)
graph = [[] for i in range(n+1)]
#graph = []
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
#print(graph)


visited_b = [False] * (n+1)
visited_d = [False] * (n+1)




def bfs(graph, start, visited_b):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited_b[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:

            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True



def dfs(graph, v, visited_d):
    # 현재 노드를 방문 처리
    visited_d[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited_d[i]:
            dfs(graph, i, visited_d)




#print('\n')
dfs(graph,num,visited_d)
print()
bfs(graph,num,visited_b)