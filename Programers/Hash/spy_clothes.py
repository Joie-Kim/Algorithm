def solution(clothes):
    answer = 1
    type_dic = {}
    
    for items in clothes:
        try: type_dic[items[1]] += 1
        except: type_dic[items[1]] = 1

    for cnt in type_dic.values():
        answer *= (cnt+1)
    
    return answer - 1