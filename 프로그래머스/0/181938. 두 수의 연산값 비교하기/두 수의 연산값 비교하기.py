def solution(a, b):
    answer = 0
    
    temp_str = str(a)+str(b)
    temp_int = 2*a*b
    
    if(int(temp_str)>=temp_int):
        answer = int(temp_str)
    else:
        answer = temp_int
    
    
    
    return answer