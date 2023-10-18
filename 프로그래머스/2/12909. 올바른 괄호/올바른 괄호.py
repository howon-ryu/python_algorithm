def solution(s):
    answer = True
    lis_s = list(s)
    stack = []
    
    for i in lis_s:
        
        
        if(len(stack) == 0):
            stack.append(i)
            print(i)
        else:
            if(stack[-1] == '('):
                if(i == ')'):
                    stack.pop()
                else:
                    stack.append(i)
            
    print(stack,len(stack))
    if(len(stack)==0):
        answer =True
    else:
        answer =False
    
    
    

    return answer