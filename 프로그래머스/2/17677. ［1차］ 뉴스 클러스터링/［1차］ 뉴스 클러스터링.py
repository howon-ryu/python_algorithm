
def solution(str1, str2):
    answer = 0
    str1_list = []
    str2_list = []
    
    for i in range(0,len(str1)-1):
        str1_up_regex=str1[i:i+2].upper()
        if(str1_up_regex.isalpha()):
            str1_list.append(str1[i:i+2].upper())
    for i in range(0,len(str2)-1):
        
        str2_up_regex=str2[i:i+2].upper()
        if(str2_up_regex.isalpha()):
            str2_list.append(str2[i:i+2].upper())
    intersection = []
    union = []
    
    for i in str1_list:
        
        if(i in str2_list):
            intersection.append(i)
            str2_list.remove(i)
            
    for i in intersection:
        if (i in str1_list):
            str1_list.remove(i)
        
    print(intersection)        
    print(str1_list)        
    print(str2_list)        
    for i in str1_list:
        union.append(i)
    for i in str2_list:
        union.append(i)
    for i in intersection:
        union.append(i)
    
    
    
    
    
    
    if(len(union)==0):
        answer = 1 *65536
    else:
        answer = int(len(intersection)/len(union)*65536)
    return answer