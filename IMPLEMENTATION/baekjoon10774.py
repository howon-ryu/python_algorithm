import sys

j = int(sys.stdin.readline().rstrip())
a = int(sys.stdin.readline().rstrip())

size_dic = {'S': 0, 'M': 1, 'L': 2}
jersey = {}
for i in range(j):
    size = sys.stdin.readline().rstrip()
    jersey[i + 1] = jersey.setdefault(i + 1, size_dic[size])

player = [list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(a)]

received = {}
ans = 0
for i in player:
    size, number = i[0], int(i[1])
    # 저지의 번호가 일치하고 선수가 원하는 사이즈와 같거나 크다면..
    if size_dic[size] <= jersey[number]:
        # 저지 딕셔너리 초기화, 해당 사이즈의 저지는 1개 있다.
        received[number] = received.setdefault(number, 1)
        # 번호의 저지가 아직 남아있다면..
        if received[number] == 1:
            ans += 1
            received[number] -= 1

print(ans)
