def solution(s):
    answer = ''
    s_list = list(s)
    print(s_list)
    for i in range(len(s_list)):
        if(i == 0):
            s_list[i] = s_list[i].upper()
        else:
            if(s_list[i] == ' ' and i!=len(s_list)-1):
                s_list[i+1] = s_list[i+1].upper()
            if(s_list[i-1]!=' '):
                s_list[i] = s_list[i].lower()
    answer = ''.join(s_list)
    return answer