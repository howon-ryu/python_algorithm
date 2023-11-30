def solution(cipher, code):
    answer = ''
    temp2 = []
    temp = list(cipher)
    for i in range(len(temp)+1):
        if(i!=0):
            
            if(i%code==0):
                print(i)
                temp2.append(temp[i-1])
    answer = ''.join(temp2)
        
    return answer