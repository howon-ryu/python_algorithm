from collections import deque
import copy


n = int(input())
p1,p2 = map(int,input().split())
m = int(input())
#print(n,m, num)
graph = [[] for i in range(n+1)]
#graph = []
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited_d = [False] * (n+1)
global abc
abc = -1
def dfs(graph, v, visited,aa):
    global abc
    # 현재 노드를 방문 처리
    aaa = aa
    aaa +=1
    #print("aaa", aaa,v)
    visited[v] = True
    if(v == p2):
        abc = aaa-1
        #print(abc)
    #print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited,aaa)
    aaa =0
#
#
#
#
# def bfs(graph, start, visited_b):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     num = 0
#     # 현재 노드를 방문 처리
#     visited_b[start] = True
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하나의 원소를 뽑아 출력
#         v = queue.popleft()
#         print("v",v,end = ' ')
#         num +=1
#         # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#         for i in graph[v]:
#
#             if not visited_b[i]:
#                 if(i == p2):
#
#
#                     return num
#                 else:
#                     queue.append(i)
#                     visited_b[i] = True
#
#
#
#
#
#

dfs(graph,p1,visited_d,0)

print(abc)