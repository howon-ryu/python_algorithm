def solution(num_list):
    answer = 0
    temp_sum = 0
    temp_gob = 1
    for i in num_list:
        temp_sum+=i
        temp_gob*=i
    #print(temp_sum*temp_sum,temp_gob)
    if(temp_sum*temp_sum>temp_gob):
        answer =1
    
    
    
    return answer