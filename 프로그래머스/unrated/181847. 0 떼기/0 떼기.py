def solution(n_str):
    answer = ''
    flag = 0
    aa = []
    n_list = list(n_str)
    print(n_list)
    for i in n_list:
        if(i == "0"):
            if(flag != 0):
                aa.append(i)
        else:
            flag = 1
            aa.append(i)
    print(aa)
    answer = ''.join(aa)
    return answer