from collections import deque

# BFS 함수 정의
# 시간 복잡도 O(n+e) v: 노드 수 , e : 간선수
def bfs():
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    # 현재 노드를 방문 처리
    queue.append((home_x,home_y))
    # 큐가 빌 때까지 반복
    while queue:

        x,y = queue.popleft()
        if((abs(x-fes_x)+abs(y-fes_y))<=1000):
            print("happy")
            return

        for i in range(n):

            if not visited[i]:
                new_x, new_y = graph[i]
                if((abs(x-new_x)+abs(y-new_y))<=1000):

                    queue.append((new_x,new_y))
                    visited[i] = 1
    print("sad")
    return



t = int(input())
for _ in range(t):
    n = int(input())
    home_x,home_y = map(int, input().split())
    graph = []
    for _ in range(n):
        x,y = map(int, input().split())
        graph.append((x,y))
    fes_x, fes_y = map(int, input().split())
    visited = [0 for _ in range(n+1)]
    bfs()













