import sys

input = sys.stdin.readline

n,k = map(int,input().split())
points = list(map(int,input().split()))


low = 0
candy_cnt = 0


high = max(points)



while low<=high:
    mid = (low+high)//2

    candy_sum = 0
    for i in points:
        if(i>=mid):
            candy_sum+=i-mid

    if(candy_sum<=k):

        high = mid-1
        candy_cnt = mid

    elif (candy_sum>k):

        low = mid+1



print(candy_cnt)