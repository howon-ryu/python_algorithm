def make(arr,com):
    sorted_arr = arr[com[0]-1:com[1]]
    sorted_arr.sort()
    return sorted_arr[com[2]-1]

def solution(array, commands):
    
    
    answer = []
    for i in range(len(commands)):
        a=make(array,commands[i])
        answer.append(a)
    
    
    return answer