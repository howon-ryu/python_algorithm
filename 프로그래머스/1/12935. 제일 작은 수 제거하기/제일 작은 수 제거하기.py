def solution(arr):
    answer = []
    min_num = min(arr)
    arr.remove(min_num)
    if(len(arr) == 0):
        answer.append(-1)
    else:
        for i in arr:
            answer.append(i)
    
    return answer