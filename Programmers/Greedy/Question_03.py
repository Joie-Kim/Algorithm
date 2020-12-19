def solution(number, k):
    idx = 0
    max_list = []
    answer = ''
    
    new_length = len(number) - k
    while True:
        if len(max_list) == new_length:
            answer = ''.join(max_list)
            return answer
        
        if '9' in number[idx:k+1]:
            max_item = '9'
        else:
            max_item = max(number[idx:k+1])
        
        max_list.append(max_item)

        idx += number[idx:k+1].index(max_item) + 1
        k += 1


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))