def solution(s):
    answer = ''
    s_list = list(s.split(' '))
    s_list_int = []
    for i in s_list:
        s_list_int.append(int(i))
    answer += str(min(s_list_int))
    answer += ' '
    answer += str(max(s_list_int))
    return answer