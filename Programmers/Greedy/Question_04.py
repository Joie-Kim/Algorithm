# 효율성 테스트 통과 못 함

def solution(people, limit):
    answer = 0

    while len(people) != 0:
        pmax = max(people)
        people.remove(pmax)

        if pmax != limit and len(people) != 0:
            pmin = min(people)
            if pmax + pmin <= limit:
                people.remove(pmin)
        
        answer += 1
    
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 50, 80], 100))
print(solution([80, 90, 30, 10, 20, 70], 100))
print(solution([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], 100))