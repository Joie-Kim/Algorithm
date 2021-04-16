def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    print(citations)
    
    for i in range(len(citations)):
        if citations[i] <= i+1:
            if citations[i] < i:
                answer = i
                break
            answer = citations[i]
            break
        answer = len(citations)
    return answer

c1 = [3, 0, 6, 1, 5]
c2 = [1, 12, 11, 9, 10, 8]
c3 = [1, 6, 6, 6, 6, 6]
c4 = [21, 20, 23, 22]
c5 = [4, 4, 4]

print(solution(c1))
print(solution(c2))
print(solution(c3))
print(solution(c4))
print(solution(c5))