import sys
input = sys.stdin.readline



n = int(input())
vote = []
cnt = 0
my = int(input())
if(n==1):
    print(0)
    exit(0)
for _ in range(n-1):
    vote.append(int(input()))

# if(max(vote)>=my):
#         print(vote.index(max(vote)))
while True:
    if(max(vote)>=my):
        vote[vote.index(max(vote))]-=1
        my+=1

        cnt+=1
    else:
        break
print(cnt)
