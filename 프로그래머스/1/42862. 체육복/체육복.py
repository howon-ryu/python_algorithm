def solution(n, lost, reserve):
    answer = 0
    answer_2 = 0
    answer_3 = 0
    li = [1 for i in range(n)]
    print(li)
    for i in reserve:
        if(li[i-1]==1):
            li[i-1]+=1
    for i in lost:
        if(li[i-1]>=1):
            #print(li[i-1])
            li[i-1]-=1
            #print(li[i-1])
    print(li)
    
    li_2=backfront(li[:])
    li_3=frontback(li[:])
    
    for i in li_2:
        if(i!=0):
            answer_2 +=1
    for i in li_3:
        if(i!=0):
            answer_3 +=1
    print(answer_2,answer_3)
    answer = max(answer_2,answer_3)
    return answer



def backfront(li):
    for i in range(len(li)):
        if(li[i]==0):
            if(i!=0):
                if(li[i-1]==2):
                    li[i-1]-=1
                    li[i]+=1
    for i in range(len(li)):
        if(li[i]==0):
            if(i!=len(li)-1):
                if(li[i+1]==2):
                    li[i+1]-=1
                    li[i]+=1
    return li
def frontback(li):
    for i in range(len(li)):
        if(li[i]==0):
            if(i!=len(li)-1):
                if(li[i+1]==2):
                    li[i+1]-=1
                    li[i]+=1
    for i in range(len(li)):
        if(li[i]==0):
            if(i!=0):
                if(li[i-1]==2):
                    li[i-1]-=1
                    li[i]+=1
    return li
    
    
    
    