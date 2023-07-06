n = int(input())

for i in range(n):
    t = int(input())

    temp = list(map(int,input().split()))
    print(min(temp),max(temp))