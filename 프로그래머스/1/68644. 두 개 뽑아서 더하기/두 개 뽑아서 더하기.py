def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    print(answer)
    
    answer_a = list(set(answer))
    answer_a.sort()
    #print(answer_a)
    return answer_a