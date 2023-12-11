def solution(myString):
    answer = ''
    re = []
    li = list(myString)
    for i in li:
        if(i=='a' or i =='A'):
            re.append(i.upper())
        else:
            re.append(i.lower())
    answer = ''.join(re)
    return answer