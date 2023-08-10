import sys

input = sys.stdin.readline


odd = []

for i in range(7):
    temp = int(input())
    if(temp%2==1):
        odd.append(temp)
odd.sort()

if(len(odd)==0):
    print(-1)
else:
    print(sum(odd))
    print(min(odd))
