import sys
input = sys.stdin.readline

n,m  = map(int,input().split())

dict1 = {}
for _ in range(n):
    girl = input().rstrip()

    mem_cnt = int(input())
    temp = []
    for i in range(mem_cnt):
        mem = input().rstrip()

        temp.append(mem)
    temp.sort()
    dict1[str(girl)] = temp

for i in range(m):
    quiz = input().rstrip()
    quiz_kind = int(input())
    if (quiz_kind == 0):
        temp = dict1[str(quiz)]
        for i in temp:
            print(i)
    elif (quiz_kind == 1):
        print(*[k for k, v in dict1.items() if quiz in v])







