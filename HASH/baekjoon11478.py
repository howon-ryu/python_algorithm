import sys
#n,m = map(int,input().split())
s = input()
#print(s)
dict1 = {}


for i in range(1,len(s)+1):
  #  print("i",i)
    for j in range(0,len(s)+1):
 #       print(s[j:i])
        if(s[j:i] != ''):
            dict1[str(s[j:i])] = 1
#print(dict1)
print(len(dict1))

