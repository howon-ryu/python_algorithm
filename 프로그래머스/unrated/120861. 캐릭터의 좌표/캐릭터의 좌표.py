def solution(keyinput, board):
    answer = [0,0]
    point = [0,0]
    for i in keyinput:
        if(i == "left"):
            if(abs(point[0]-1)<=board[0]//2):
                point[0] = point[0]-1
        elif(i == "right"):
            if(abs(point[0]+1)<=board[0]//2):
                point[0] = point[0]+1
        elif(i == "up"):
            if(abs(point[1]+1)<=board[1]//2):
                point[1] = point[1]+1
        elif(i == "down"):
            if(abs(point[1]-1)<=board[1]//2):
                point[1] = point[1]-1
    print(point)
    print(board)
    
        
    answer = point
    
    return answer




def bu(prop):
    if prop>=0:
        return 1
    
    elif prop<0:
        return -1
 
