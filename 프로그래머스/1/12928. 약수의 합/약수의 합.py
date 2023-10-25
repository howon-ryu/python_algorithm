def solution(n):
    answer = 0
    answer = yy(n)
    return answer


def yy(num):
    temp = 0
    for i in range(1,num+1):
        if(num%i==0):
            temp+=i
    return temp