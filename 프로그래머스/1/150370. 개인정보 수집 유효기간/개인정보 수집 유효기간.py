def solution(today, terms, privacies):
    answer = []
    cal = []
    dur = []
    new = []
    to = list(today.split('.'))
    lux1 = dict() 
    for i in privacies:
        t=i.split(' ')
        cal.append(t[0])
        dur.append(t[1])
    #print(cal,dur)
    
    for i in terms:
        t = i.split(' ')
        lux1[t[0]] = t[1]
    #print(lux1)
    
    for i in range(len(dur)):
        #print(lux1[dur[i]])
        
        tt = cal[i].split('.')
        yy = int(tt[0])*336
        mm = int(tt[1])*28
        dd = int(tt[2])+int(lux1[dur[i]])*28-1
        
        too = int(to[0])*336+int(to[1])*28+int(to[2])
        ttt = yy+mm+dd
        print(too,ttt)
        if(too>ttt):
            answer.append(i+1)
#         yy = int(tt[0])
#         mm = int(tt[1])+int(lux1[dur[i]])
#         dd = int(tt[2])-1
        
#         if(dd==0):
#             mm = mm-1
#             if(mm>12):
#                 mm=mm-12

#                 yy=yy+1
#             dd =28
#         else:
#             if(mm>12):
#                 mm=mm-12

#                 yy=yy+1
                
#         print(today,str(yy)+"."+str(mm)+"."+str(dd))
        
#         if(int(to[0])<=yy):
#             if(int(to[1])<=mm):
                
#                 if(int(to[2])>dd):
                    
#                     answer.append(i+1)
                
#                     print(i+1)
            
               
#             else:
#                 answer.append(i+1)
#                 print(i+1)
                   
#         else:
            
#             answer.append(i+1)
#             print(i+1)
        
            
        
    
    
    return answer