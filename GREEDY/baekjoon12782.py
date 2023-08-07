import sys


input = sys.stdin.readline

t = int(input())


for _ in range(t):
    one_cnt = 0
    zero_cnt = 0
    one,two = map(list,input().split())
    for i in range(len(one)):
        if(one[i] != two[i]):
            if(one[i]=='1'):
                one[i] = '0'
                zero_cnt+=1
            elif(one[i]=='0'):
                one[i] = '1'
                one_cnt += 1
    if(one_cnt<=zero_cnt):
        zero_cnt= zero_cnt-one_cnt

        print(zero_cnt+one_cnt)
    else:
        one_cnt=one_cnt-zero_cnt

        print(zero_cnt + one_cnt)




