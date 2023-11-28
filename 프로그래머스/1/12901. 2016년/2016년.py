def solution(a, b):
    answer = ''
    mon = {'1':0,'2':31,'3':60,'4':91,'5':121,'6':152,'7':182,'8':213,'9':244,'10':274,'11':305,'12':335}
    dayy = mon[str(a)]+b
    print(dayy//7,dayy%7)
    if(dayy%7 == 0):
        answer = 'THU'
    elif(dayy%7 == 1):
        answer = 'FRI'
    elif(dayy%7 == 2):
        answer = 'SAT'
    elif(dayy%7 == 3):
        answer = 'SUN'
    elif(dayy%7 == 4):
        answer = 'MON'
    elif(dayy%7 == 5):
        answer = 'TUE'
    elif(dayy%7 == 6):
        answer = 'WED'

    return answer