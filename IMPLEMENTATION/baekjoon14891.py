import sys
input = sys.stdin.readline

first_wheel = list(input().rstrip())
second_wheel = list(input().rstrip())
third_wheel = list(input().rstrip())
fourth_wheel = list(input().rstrip())


def right_spin(num,flag):
    if(num==1):
        if (first_wheel[2] != second_wheel[6] and (flag ==2 or flag==5)):
            left_spin(2, 3)
        first_wheel.insert(0, first_wheel[-1])
        del first_wheel[-1]
    elif(num==2):

        if (first_wheel[2] != second_wheel[6] and (flag ==1 or flag==5)):
            left_spin(1, 0)
        if (second_wheel[2] != third_wheel[6] and (flag ==3 or flag==5)):
            left_spin(3, 4)

        second_wheel.insert(0, second_wheel[-1])
        del second_wheel[-1]
    elif (num == 3):
        if (second_wheel[2] != third_wheel[6] and (flag ==2 or flag==5)):
            left_spin(2, 1)
        if (third_wheel[2] != fourth_wheel[6] and (flag ==4 or flag==5)):
            left_spin(4, 0)
        third_wheel.insert(0, third_wheel[-1])
        del third_wheel[-1]
    elif (num == 4):
        if (third_wheel[2] != fourth_wheel[6] and (flag ==3 or flag==5)):
            left_spin(3, 2)
        fourth_wheel.insert(0, fourth_wheel[-1])
        del fourth_wheel[-1]


def left_spin(num,flag):
    if (num == 1):

        if (first_wheel[2] != second_wheel[6] and (flag == 2 or flag == 5)):
            right_spin(2, 3)


        first_wheel.append(first_wheel[0])
        del first_wheel[0]
    elif (num == 2):

        if (first_wheel[2] != second_wheel[6] and (flag == 1 or flag == 5)):
            right_spin(1, 0)
        if (second_wheel[2] != third_wheel[6] and (flag == 3 or flag == 5)):
            right_spin(3, 4)

        second_wheel.append(second_wheel[0])
        del second_wheel[0]
    elif (num == 3):
        if(second_wheel[2] != third_wheel[6] and (flag ==2 or flag==5) ):
            right_spin(2,1)
        if(third_wheel[2]!=fourth_wheel[6] and (flag ==4 or flag==5)):
            right_spin(4,0)

        third_wheel.append(third_wheel[0])
        del third_wheel[0]




    elif (num == 4):

        if (third_wheel[2] != fourth_wheel[6] and (flag == 3 or flag == 5)):
            right_spin(3, 2)
        fourth_wheel.append(fourth_wheel[0])
        del fourth_wheel[0]


k = int(input())

for _ in range(k):
    wheel,dir = map(int,input().split())
    if(dir ==1):
        right_spin(wheel,5)
    elif(dir ==-1):
        left_spin(wheel,5)




res = 0




res = int(first_wheel[0])+int(second_wheel[0])*2+int(third_wheel[0])*4+int(fourth_wheel[0])*8

print(first_wheel)
print(second_wheel)
print(third_wheel)
print(fourth_wheel)

print(res)