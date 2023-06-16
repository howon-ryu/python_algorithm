import sys

n,m = map(int,input().split())

dict1 = {}
dict2 = {}
# def get_key(val):
#     for key, value in dict1.items():
#
#          if val == value:
#
#              return key
for i in range(n):
    value = input()
    dict1[str(i+1)] = value
    dict2[str(value)] = i+1

# print(dict1)
for i in range(m):
    temp = input()
    if(temp.isnumeric()):
        print(dict1[str(temp)])
    else:
        print(dict2[str(temp)])

