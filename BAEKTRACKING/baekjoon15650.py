from itertools import permutations



n,m = map(int,input().split())
list_n = [i for i in range(1,n+1)]
#print(list_n)
#print(list_n,m)
dict1 = []
for i in permutations(list_n, m):

    temp = list(i)

    temp.sort()
    if(temp not in dict1):
        print(*temp, end = "\n")
        dict1.append(temp)



    # for j in list(i):
    #
    #     print(j, end=" ")
    # print()
    # print(i[0],i[1], end="\n")