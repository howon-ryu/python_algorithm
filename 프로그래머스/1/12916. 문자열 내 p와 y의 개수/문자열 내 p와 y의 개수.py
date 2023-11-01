def solution(s):
    answer = True
    count_p = 0
    count_y = 0
    s_list = list(s)
    for i in s_list:
        if(i == 'p' or i == 'P'):
            count_p+=1
        elif(i == 'y' or i == 'Y'):
            count_y+=1
    print(count_p,count_y)
    if(count_p==count_y):
        answer = True
    else:
        answer = False
    print(answer)
        
        

    return answer