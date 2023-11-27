def solution(food):
    answer = ''
    answer_list = []
     
    zero = 0
    for i in range(len(food)):
        if(i==0):
            zero = food[i]
        else:
            
            for j in range(food[i]//2):
                answer_list.append(i)
    answer_relist = answer_list[:]
    answer_relist.reverse()
    
    answer = ''.join(map(str,answer_list))+'0'*zero+''.join(map(str,answer_relist))
    
    #print(answer_list,answer_relist)
    return answer