def solution(common):
    answer = 0
    if(common[0]!=0 and common[1]!=0):
        one= common[0]
        two= common[1]
        three= common[2]
        two_one_minus = two-one
        two_one_divide =  two/one
        three_two_minus = three-two
        three_two_divide =  three/two

        if(three_two_minus == two_one_minus):
            answer = common[len(common)-1]+two_one_minus
        elif (three_two_divide == two_one_divide):

            answer = common[len(common)-1]*two_one_divide
    else:
        one= common[0]
        two= common[1]
        three= common[2]  
        two_one_minus = two-one
        
        answer = common[len(common)-1]+two_one_minus
    
    return answer