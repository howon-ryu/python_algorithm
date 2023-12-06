def solution(myString):
    answer = []
    myString=myString.replace('x',' ')
    
    al = myString.split(' ')
    
    for i in al:
        if(i!='' and i != ' '):
            
            answer.append(i)
    answer.sort()
    return answer