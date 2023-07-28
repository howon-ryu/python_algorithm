
n,m = map(int,input().split())

j = int(input())

cnt = 0
start = 1
end = start+(m-1)


for _ in range(j):
    apple = int(input())
    if(apple>=start and apple<=end)
        continue
    elif(apple>end):
        temp = apple-end
        cnt+=temp
        end+=temp
        start+=temp
    elif(apple<start):
        temp = start-apple
        cnt+=temp
        end-=temp
        start-=temp
print(cnt)