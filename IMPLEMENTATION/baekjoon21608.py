import sys

input = sys.stdin.readline
dict1 = {}
n = int(input())
last=0
classroom = [[0]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def crosscheck(x,y,num):

    like_list = dict1[str(num)]
    cnt = 0
    blank_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx < 0 or nx >= n or ny < 0 or ny >= n):
            continue
        if(classroom[nx][ny]==0):
            blank_cnt+=1
        if (int(classroom[nx][ny]) in like_list):
            cnt+=1


    return x,y,cnt,blank_cnt


for stu_input in range(n*n):
    temp = list(map(int,input().split()))
    stu = temp[0]
    if(stu_input==n*n-1):
        last = stu
    del temp[0]

    dict1[str(stu)]=temp



def seatchoice(num):
    res_x=n*n+1
    res_y =n*n+1
    res_cnt =0
    res_blank = 0
    for i in range(n):
        for j in range(n):
            if(classroom[i][j]==0):

                t_x,t_y,t_cnt,t_blank=crosscheck(i,j,num)
                # print(t_x,t_y,t_cnt,t_blank)
                if(t_cnt>res_cnt):
                    res_x = t_x
                    res_y = t_y
                    res_cnt=t_cnt
                    res_blank = t_blank
                elif (t_cnt==res_cnt):
                    if(t_blank>res_blank):
                        res_x = t_x
                        res_y = t_y

                        res_blank = t_blank

                    elif(t_blank==res_blank):

                        if(t_x<res_x):
                            res_x = t_x
                            res_y = t_y
                        elif(t_x==res_x):

                            if(t_y<res_y):
                                res_x = t_x
                                res_y = t_y

                if (num == str(last)):
                    res_x = t_x
                    res_y = t_y


    return res_x,res_y







for i in list(dict1.keys()):


    seat_x,seat_y = seatchoice(i)
    classroom[seat_x][seat_y] = str(i)
    # print(classroom)
    # print("x",seat_x,"y",seat_y)

res = 0

for i in range(n):
    for j in range(n):

        t_x, t_y, t_cnt, t_blank = crosscheck(i, j, classroom[i][j])
        if(t_cnt==1):
            res+=1
        elif(t_cnt==2):
            res+=10
        elif (t_cnt == 3):
            res += 100
        elif (t_cnt == 4):
            res += 1000






# print(dict1)
print(res)