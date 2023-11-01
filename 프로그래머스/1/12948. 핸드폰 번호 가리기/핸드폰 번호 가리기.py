def solution(phone_number):
    answer = ''
    p_list = list(phone_number)
    p_list.reverse()
    ll = []
    print(p_list)
    for i in range(len(p_list)):
        if(i<4):
            ll.append(p_list[i])
        else:
            ll.append('*')
    ll.reverse()
    answer = ''.join(ll)
    
    return answer