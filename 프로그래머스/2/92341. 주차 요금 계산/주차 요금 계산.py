import math
def make_min(val):
    val_str = val.split(':')
    minute = int(val_str[0]) * 60 + int(val_str[1])
    return minute


def solution(fees, records):
    answer = []
    dic = {}
    dic_min = {}
    #print(fees)
    #print(records)
    for i in records:
        strr = i.split(' ')
        dic[strr[1]] = 0
        dic_min[strr[1]] = 0
    
    
    for i in records:
        strr = i.split(' ')
        
        if (strr[2] == 'IN'):
            dic[strr[1]] = make_min(strr[0])
            
        else:
            #print("abc",strr)   
            
            dic_min[strr[1]] = dic_min[strr[1]]+make_min(strr[0])-dic[strr[1]]
            dic[strr[1]] = 0
            #print("abc",dic_min)   
    for i in dic.items():
        
        if(i[1]>0):
            
            dic_min[i[0]] = dic_min[i[0]]+make_min('23:59')-dic[i[0]]
        elif(i[1]==0):
            for j in records:
                strr2 = j.split(' ')
                if(strr2[1]==i[0]):
                    
                    if(strr2[0]=='00:00' and dic_min[i[0]]==0):
                        dic_min[i[0]] = make_min('23:59')-make_min('00:00')
    #print(dic)
    #print(dic_min)
    
    d1 = sorted(dic_min.items())
    
    for i in d1:
        if(i[1]<=fees[0]):
            answer.append(fees[1])
        else:
            #print(i[1],fees[0],fees[2],fees[3],fees[1],math.ceil((i[1]-fees[0])/fees[2]))
            middle =i[1]-fees[0]
            if(middle%fees[2]==0):
                answer.append((middle/fees[2])*fees[3]+fees[1])
            else:
                #answer.append((((((i[1]-fees[0])+9)//10)*10)/fees[2])*fees[3]+fees[1])   
                answer.append(math.ceil((i[1]-fees[0])/fees[2])*fees[3]+fees[1])
            #answer.append((((((i[1]-fees[0])+9)//10)*10)/fees[2])*fees[3]+fees[1])
    return answer