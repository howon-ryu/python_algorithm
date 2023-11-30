def solution(my_string):
    answer = ''
    temp2 = []
    temp = list(my_string)
    print(temp)
    for i in temp:
        if(i.isupper()):
            varr = i.lower()
            temp2.append(varr)
        else:
            varr = i.upper()
            temp2.append(varr)
    answer = ''.join(temp2)
    return answer