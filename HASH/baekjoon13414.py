import sys
n,m = map(int,input().split())

dict1 = {}



for i in range(m):
    value = sys.stdin.readline().strip()
    # dict1[str(i+1)] = value
    dict1[str(value)] = i+1
#print(dict1)

sorted_dict1 = sorted(dict1.items(), key = lambda item: item[1])
#print(sorted_dict1[0][0])


for i in range(n):
    if(i<len(sorted_dict1)):
        #print(i,len(sorted_dict1))
        print(sorted_dict1[i][0])
#
# for i in range(num):
#     key,value = map(str,input().split())
#     dict1[key] = value
#
# lili=[]
#
# for i in dict1:
#
#     if(dict1[i]=="enter"):
#         lili.append(i)
#
# lili.sort(reverse=True)
# for i in lili:
#     print(i)