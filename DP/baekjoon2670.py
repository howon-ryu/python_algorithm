


n = int(input())
li = []

for i in range(n):
    tmp = float(input())
    li.append(tmp)



for i in range(1,len(li)):

    li[i] = max(li[i-1]*li[i],li[i])

print("%0.3f"% max(li))