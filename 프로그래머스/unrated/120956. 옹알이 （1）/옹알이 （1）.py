def solution(babbling):
    answer = 0
    listt = ["aya","ye","woo","ma"]
    
    
    
    
    for i in babbling:
        
        new = i
        for j in listt:
            new = new.replace(j,' ')
        
        print(len(new.strip()))
        if(len(new.strip())==0):
            answer +=1
        
    
    return answer