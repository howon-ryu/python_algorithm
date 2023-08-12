import sys
input = sys.stdin.readline

n = int(input())
money = list(map(int, input().split()))
max_money = int(input())


start = 1
end = max(money)
answer = 0
while start <= end:
    mid = (start+end)//2
    c = 0 # 길이가 mid인 것을 만들 수 있는 개수





    for i in money:
        if(i//mid>=1):
            c+=mid
        else:
            c+=i

    if c <=max_money:
        answer = max(answer,mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)