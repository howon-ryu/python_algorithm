import sys
n,m = map(int,input().split())
# m = int(input())
#
# for o in range(m):
#     n = int(input())
#     dict1 = {}
#     for i in range(n):
#         fashion, position = map(str, input().split())
#         if (position in dict1):
#             dict1[position] +=1
#         else:
#             dict1[position] = 1
#     result = 1
#     for count in dict1.values():
#         result *= count +1
#         #print(count)
#     result -=1
#     print(result)

dict1 = {}
result = 0
a = list(map(int,input().split()))
b= list(map(int,input().split()))
#print(a,b)
for i in a:
    if(str(i) in dict1):
        dict1[str(i)]+=1
    else:
        dict1[str(i)] = 1
for i in b:
    if(str(i) in dict1):
        dict1[str(i)]+=1
    else:
        dict1[str(i)] = 1
for i in dict1:
    #print("i",i,dict1[str(i)])
    if(dict1[str(i)]==1):
        result+=1
print(result)