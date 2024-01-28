def solution(a, b):
    answer = 0
    plus_one = str(a)+str(b)
    plus_two = str(b)+str(a)
    if(int(plus_one) >int(plus_two)):
        answer = int(plus_one)
    elif(int(plus_one) <int(plus_two)):
        answer = int(plus_two)
    else:
        answer = int(plus_one)
    
    
    
    return answer