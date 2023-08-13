import sys

input = sys.stdin.readline


while True:
    n,m = map(int, input().split())
    if(n==0 and m==0):
        break
    a = []
    b = []
    for _ in range(n):
        a.append(int(input()))
    for _ in range(m):
        b.append(int(input()))
    cnt = 0
    for card in a:
        low,high = 0,len(b)-1
        exist = False
        while low<=high:
            mid = (low + high) // 2
            if(b[mid]>card):
                high = mid - 1
            elif (b[mid]<card):
                low = mid+1
            else:
                cnt+=1
                exist=True
                break






    print(cnt)
