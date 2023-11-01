def fucc(s):
    s_list = list(s)
    none_zero = []
    zero_cnt = 0
    for i in s_list:
        if (i == '0'):
            zero_cnt +=1
        else:
            none_zero.append(i)
    str_none_zero = ''.join(none_zero)
    return str_none_zero,zero_cnt

def solution(s):
    answer = [0,0]
    z_cnt = 0
    cnt = 0
    flag = True
    while (flag):
        t_s = list(s)
        
        
        if(s != '1'):
            
            new_s, zz = fucc(s)
            s = format(len(new_s), '#b')
            answer[0]+=1
            answer[1]+=zz
            s = s[2:]
            #print(s)
            #flag = False
        else:
            flag = False
        
    
        
    
        
    #print(new_s,zz)
    
    return answer