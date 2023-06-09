from collections import deque
import copy
n = int(input())
miro = []

for _ in range(n):
  miro.append(list(map(int, input())))


def bfs(x, y,list_k):
    aa = 0
    vi = []
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    if(list_k[x][y]!=0):

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque()

        queue.append((x,y))

        aa+=1
        vi.append((x, y))
        # print("!!",aa)
        # 현재 노드를 방문 처리

        # 큐가 빌 때까지 반복
        while queue:
            x,y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(nx<0 or nx>=n or ny<0 or ny>=n):
                    continue
                if(list_k[nx][ny]==0):
                    continue
                if(list_k[nx][ny] == 1):
                    # print("x", nx, "y", ny)
                    vi.append((nx,ny))
                    aa+=1
                    list_k[nx][ny] = list_k[x][y]+ 1
                    queue.append((nx, ny))
    # print(miro)
    # print(list_cp)
    # print(list_k)

    if(aa == 0):
        return 0,vi
    elif (aa == 1):

        return 1,vi
    else:
        return aa-1,vi



home = []
vvv = []
# list_cp = copy.deepcopy(miro)
# print(bfs(0,1,list_cp))
# list_cp = copy.deepcopy(miro)
# print(bfs(0,2,list_cp))
for j in range(n):
    for k in range(n):
        list_cp = copy.deepcopy(miro)
        if((j,k) not in vvv):
            # print(j, k, vvv)
            temp,visited = bfs(j,k,list_cp)

            for kkk in visited:

                vvv.append(kkk)
        # print(temp)
        #else:
            # print("??",(j,k),temp)
        if(temp!=0):

            # print("temp",temp)
            home.append(temp)
            temp = 0





home.sort()
print(len(home))
print(*home,sep = '\n')



