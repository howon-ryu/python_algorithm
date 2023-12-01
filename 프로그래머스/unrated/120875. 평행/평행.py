def solution(dots):
    answer = 0
    for i in range(1,len(dots)):
        tt = [1,2,3]
        
        if(dots[i][0]>dots[0][0]):
            temp1x = dots[i][0]-dots[0][0]
            if(dots[i][1]>dots[0][1]):
                temp1y = dots[i][1]-dots[0][1]
            else:
                temp1y = dots[0][1]-dots[i][1]
        else:
            temp1x = dots[0][0]-dots[i][0]
            if(dots[i][1]>dots[0][1]):
                temp1y = dots[i][1]-dots[0][1]
            else:
                temp1y = dots[0][1]-dots[i][1]
        tt.remove(i)
        if(dots[tt[0]][0]>dots[tt[1]][0]):
            temp2x = dots[tt[0]][0]-dots[tt[1]][0]
            
            if(dots[tt[0]][1]>dots[tt[1]][1]):
                temp2y = dots[tt[0]][1]-dots[tt[1]][1]
            else:
                temp2y = dots[tt[1]][1]- dots[tt[0]][1]
        else:
            temp2x = dots[tt[1]][0]-dots[tt[0]][0]
            
            
            if(dots[tt[0]][1]>dots[tt[1]][1]):
                temp2y = dots[tt[0]][1]-dots[tt[1]][1]
            else:
                temp2y = dots[tt[1]][1]- dots[tt[0]][1]
        print(temp1x,temp2x,temp1y,temp2y)
        print(temp1y/temp1x,temp2y/temp1y)
        if(temp1y/temp1x==temp2y/temp2x):
            answer = 1
            break
        else:
            answer = 0
            
    
    return answer