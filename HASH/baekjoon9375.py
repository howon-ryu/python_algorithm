import sys
#n,m = map(int,input().split())
m = int(input())

for o in range(m):
    n = int(input())
    dict1 = {}
    for i in range(n):
        fashion, position = map(str, input().split())
        if (position in dict1):
            dict1[position] +=1
        else:
            dict1[position] = 1
    result = 1
    for count in dict1.values():
        result *= count +1
        #print(count)
    result -=1
    print(result)
