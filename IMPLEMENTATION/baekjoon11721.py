import sys

input = sys.stdin.readline


strr = input()

for i in range(0,len(strr),10):
    print(strr[i:i+10])