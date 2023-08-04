import sys
input = sys.stdin.readline

ans = ['U','C','P','C']

str_list = list(input().replace(" ",""))


for i in str_list:

    if(i==ans[0]):
        del ans[0]
    if(len(ans)==0):
        break

if(len(ans)==0):
    print("I love UCPC")
else:
    print("I hate UCPC")
