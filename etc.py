import sys
import time
from collections import deque
from collections import Counter
from sys import stdin
#n,m = map(int, sys.stdin.readline().split())
#data = list(map(int,sys.stdin.readline().split()))
import heapq
from importlib import machinery
from fractions import Fraction
import math
#
#
# n = input()
# # n,a,b = list(map(int,input().split()))


for line in sys.stdin:
    tri = list(map(int,line.split()))
    tri.sort()
    if(tri[0] ==0 and tri[1] ==0 and tri[2] ==0):
        break

    else:
        if(tri[0]+tri[1]<=tri[2]):
            print("Invalid")
        elif(tri[0]==tri[1]==tri[2]):
            print("Equilateral")
        elif(tri[0]!=tri[1]!=tri[2]):
            print("Scalene")
        else:
            print("Isosceles")





















