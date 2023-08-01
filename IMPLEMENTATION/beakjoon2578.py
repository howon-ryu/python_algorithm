import sys
input = sys.stdin.readline

board = []

for _ in range(5):
    board.append(list(map(int,input().split())))


binggo_cnt = 0
def check(num):
    global binggo_cnt
    for i in range(5):
        for j in range(5):

            if(board[i][j]==num):
                board[i][j] = 0


                if (i == j and j==2):
                    row_sum = sum(board[i])
                    col_sum = board[0][j] + board[1][j] + board[2][j] + board[3][j] + board[4][j]
                    leftup_to_rightdown = board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4]
                    rightup_to_leftdown = board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][0]
                    if (row_sum == 0):
                        binggo_cnt+=1
                    if (col_sum == 0):
                        binggo_cnt+=1
                    if (rightup_to_leftdown == 0):
                        binggo_cnt+=1
                    if (leftup_to_rightdown == 0):
                        binggo_cnt+=1
                elif (i+j==4):
                    row_sum = sum(board[i])
                    col_sum = board[0][j] + board[1][j] + board[2][j] + board[3][j] + board[4][j]
                    rightup_to_leftdown = board[0][4]+board[1][3]+board[2][2]+board[3][1]+board[4][0]
                    if (row_sum == 0):
                        binggo_cnt+=1
                    if (col_sum == 0):
                        binggo_cnt+=1
                    if (rightup_to_leftdown == 0):
                        binggo_cnt+=1
                elif (i == j):

                    row_sum = sum(board[i])

                    col_sum = board[0][j] + board[1][j] + board[2][j] + board[3][j] + board[4][j]

                    leftup_to_rightdown = board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4]
                    if (row_sum == 0):
                        binggo_cnt += 1

                    if (col_sum == 0):
                        binggo_cnt += 1
                    if (leftup_to_rightdown == 0):
                        binggo_cnt += 1


                else:
                    row_sum = sum(board[i])

                    col_sum = board[0][j]+board[1][j]+board[2][j]+board[3][j]+board[4][j]

                    if (row_sum == 0):
                        binggo_cnt+=1
                    if (col_sum == 0):
                        binggo_cnt+=1





cnt = 0


for i in range(25):
    num_list = list(input().split())
    for i in num_list:
        cnt+=1
        check(int(i))

        if(binggo_cnt>=3):
            print(cnt)

            exit(0)


