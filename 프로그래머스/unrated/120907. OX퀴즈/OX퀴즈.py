def solution(quiz):
    answer = []
    re_arr = []
    #print(quiz[0])
    for i in quiz:
        # print(i)
        re_arr.append(i.split())
    #print(re_arr)
    for i in re_arr:
        print(i)
        
        if(i[1]=="+"):
            if(int(i[0])+int(i[2])==int(i[4])):
                answer.append("O")
            else:
                answer.append("X")
        elif(i[1]=="-"):
             if(int(i[0])-int(i[2])==int(i[4])):
                answer.append("O")
             else:
                answer.append("X")   
            
        
    
    return answer