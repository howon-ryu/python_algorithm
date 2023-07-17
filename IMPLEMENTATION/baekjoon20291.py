import sys

n = int(input())

dict1 = {}

for i in range(n):
    t,value = input().split('.')

    if (str(value) in dict1):
        dict1[str(value)] += 1
    else:
        dict1[str(value)] = 1
sorted_dict = sorted(dict1.items())
for i in sorted_dict:
    print(i[0],i[1])






