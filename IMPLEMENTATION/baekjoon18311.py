import sys
import copy
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
temp = list(map(int,input().split()))
sum = sum(temp)
li = [0]*(n+1)
li[0] =0


for i in range(1,len(temp)+1):
    li[i] = li[i-1]+temp[i-1]
li_2 = copy.deepcopy(li)
for i in range(1,len(temp)+1):
    li_2.append(li_2[len(li_2)-1]+temp[len(temp)-i])
answer = 0

if(k<=sum):
    for i in range(len(li)):
        if(li[i]>k):
            answer = i
            # print(i)
            break
else:
    for i in range(len(li_2)):
        if(li_2[i]>k):
            answer = len(temp) - (i-(len(temp)+1))
            # print(i)
            break




print(answer)