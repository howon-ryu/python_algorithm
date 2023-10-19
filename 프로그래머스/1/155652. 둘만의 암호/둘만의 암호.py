from string import ascii_lowercase






def solution(s, skip, index):
    answer = ''
    answer_list = []
    skip_list = list(skip)
    alphabet_list = list(ascii_lowercase)
    #print(alphabet_list)
    s_list = list(s)
    for i in s:
        num=alphabet_list.index(i)
        
        
        num_t = num+1
        temp = []
        tt =1
        while(tt<index+1):
            
            if(num_t>=26):
                    num_t = 0
            
            # print(num_t,alphabet_list[num_t])
            if(alphabet_list[num_t] in skip_list):
                print("over",num_t)
                num_t = num_t+1
                if(num_t>=26):
                    num_t = 0
                    
            else:
                temp.append(alphabet_list[num_t])
                num_t=num_t+1
                if(num_t>=26):
                    num_t = 0
                tt = tt+1 


        answer_list.append(temp[-1])
                
                
            
            
                
    print(answer_list)
    answer = ''.join(answer_list)
    return answer