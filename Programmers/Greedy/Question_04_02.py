# sort() 사용해서 정렬
# 효율성 테스트 통과
# 이전 코드는 매번 max(), min(), remove()를 사용해서 그랬던 것 같음

def solution(people, limit):
    answer = 0

    people.sort()

    front = 0               # 최솟값 탐색
    rear = len(people) - 1  # 최댓값 탐색

    while rear - front >= 1:
        if people[rear] + people[front] <= limit:
                front += 1   
        
        rear -= 1
        answer += 1
        
    if rear == front:
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 50, 80], 100))
print(solution([80, 90, 30, 10, 20, 70], 100))
print(solution([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], 100))