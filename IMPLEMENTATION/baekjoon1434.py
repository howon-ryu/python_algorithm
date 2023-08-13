import sys

input = sys.stdin.readline


n,m = map(int,input().split())

boxes = list(map(int,input().split()))
weight = list(map(int,input().split()))


for i in range(len(weight)):
    for j in range(len(boxes)):
        if(weight[i]<=boxes[j]):
            boxes[j]-=weight[i]
            weight[i]-=weight[i]
print(sum(boxes))
