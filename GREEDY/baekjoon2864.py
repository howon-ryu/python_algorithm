import sys

input = sys.stdin.readline

a,b = map(list,input().split())
max_a = 0
max_b = 0
min_a = 0
min_b = 0

for i in range(len(a)):
    if(a[i]=='5'):
        a[i] = '6'

for i in range(len(b)):
    if (b[i] == '5'):
        b[i] = '6'


for i in range(len(a)):
    max_a = max_a*10+int(a[i])
for i in range(len(a)):
    max_b = max_b*10+int(b[i])

for i in range(len(a)):
    if(a[i]=='6'):
        a[i] = '5'

for i in range(len(b)):
    if (b[i] == '6'):
        b[i] = '5'


for i in range(len(a)):
    min_a = min_a*10+int(a[i])
for i in range(len(a)):
    min_b = min_b*10+int(b[i])
print(min_a+min_b,max_a+max_b)

