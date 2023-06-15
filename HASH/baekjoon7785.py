num = int(input())

dict1 = {}

for i in range(num):
    key,value = map(str,input().split())
    dict1[key] = value

lili=[]

for i in dict1:

    if(dict1[i]=="enter"):
        lili.append(i)

lili.sort(reverse=True)
for i in lili:
    print(i)