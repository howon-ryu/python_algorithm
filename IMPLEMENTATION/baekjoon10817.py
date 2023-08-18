import sys

input = sys.stdin.readline

cnt = list(map(int,input().split()))

cnt.remove(max(cnt))
cnt.remove(min(cnt))


print(cnt[0])


