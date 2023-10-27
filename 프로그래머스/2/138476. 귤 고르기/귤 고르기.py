

def get_counts(seq): 
    counts = {}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def solution(k, tangerine):
    dic = get_counts(tangerine)
    sorted_dict = sorted(dic.items(), key = lambda item: item[1], reverse = True)
    tanger_list = []
    #print(sorted_dict)
    for i in sorted_dict:
        if(k == 0):
            break
        else:
            if(i[1]<k):
                tanger_list.append(i[0])
                k = k-i[1]
            else:
                tanger_list.append(i[0])
                k = 0
        #print(k)
    #print(tanger_list)
    answer = len(tanger_list)
    # sorted_dict_as_dict = {k: v for k, v in sorted_dict}
    # print(sorted_dict_as_dict)
    
    return answer