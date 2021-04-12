def solution(participant, completion):
    pHash = 0
    cHash = 0
    dic = {}
    answer = ''
    
    for part in participant:
        dic[hash(part)] = part
        pHash += hash(part)
    for comp in completion:
        cHash += hash(comp)
    answer = dic[(pHash - cHash)]
    return answer