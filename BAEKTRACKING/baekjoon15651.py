from itertools import combinations, permutations,product



n,m = map(int,input().split())
list_n = [i for i in range(1,n+1)]

#print(list_n,m)
for i in product(list_n, repeat = m):

    for j in i:
        print(j, end=" ")
    print()
    # print(i[0],i[1], end="\n")