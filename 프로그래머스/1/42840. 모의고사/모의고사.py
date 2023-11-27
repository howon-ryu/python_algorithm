def solution(answers):
    answer = []
    person_dic = {'1':0,'2':0,'3':0}
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    if(len(answers)>len(one)):
        while(len(one)<len(answers)):
            one = one+one
    if(len(answers)>len(two)):
        while(len(two)<len(answers)):
            two = two+two
    if(len(answers)>len(three)):
        while(len(three)<len(answers)):
            three = three+three
    
    for i in range(len(answers)):
        
        if(answers[i]==one[i]):
            person_dic['1'] = person_dic['1']+1
        if(answers[i]==two[i]):
            person_dic['2'] = person_dic['2']+1
        if(answers[i]==three[i]):
            person_dic['3'] = person_dic['3']+1
    
    #print(person_dic)
    answer = [int(k) for k,v in person_dic.items() if max(person_dic.values()) == v]
    
    #print(answer)

    return answer