def solution(lottos, win_nums):
    answer = []
    collect_num =0
    zero_num = 0
    for i in lottos:
        if(i!=0 and i in win_nums):
            print(i)
            collect_num+=1
    for j in lottos:
        if(j==0):
            zero_num+=1
    #print(collect_num,zero_num)
    if(collect_num+zero_num==6):
        answer.append(1)
    elif(collect_num+zero_num==5):
        answer.append(2)
    elif(collect_num+zero_num==4):
        answer.append(3)
    elif(collect_num+zero_num==3):
        answer.append(4)
    elif(collect_num+zero_num==2):
        answer.append(5)
    else:
        answer.append(6)
    if(collect_num==0):
        answer.append(6)
    else:
        
        answer.append(7-collect_num)
    return answer