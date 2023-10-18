def solution(n):
    answer = 0
    ori_cnt = 0
    b = format(n, 'b')
    list_b = list(b)
    for i in list_b:
        if(i == '1'):
            ori_cnt+=1
    #print(ori_cnt)
    while True:
        n = n+1
        bb = format(n, 'b')
        list_bb = list(bb)
        next_cnt=0
        for i in list_bb:
            if(i == '1'):
                next_cnt+=1
        if(ori_cnt==next_cnt):
            answer = n
            #exit(0)
            break
        
        
    return answer