def solution(s):
    answer = ''
    lenn = len(s)
    if(lenn %2 ==0):
        answer = s[lenn//2-1:lenn//2+1]
    else:
        answer = s[lenn//2]
    return answer