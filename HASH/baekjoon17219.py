import sys
n,m = map(int,input().split())

dict1 = {}



for i in range(n):
    # value = sys.stdin.readline().strip()
    site, pw = map(str,input().split())
    # dict1[str(i+1)] = value
    dict1[str(site)] = pw
#print(dict1)

#sorted_dict1 = sorted(dict1.items(), key = lambda item: item[1])
#print(sorted_dict1[0][0])


for i in range(m):
    temp = input()
    print(dict1[str(temp)])
