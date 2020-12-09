# 문제에 빠진 조건 : brown은 무조건 한 줄

def solution(brown, yellow):
    div = []      # yellow의 약수
    answer = []

    i = 1
    while i * i <= yellow:
        if yellow % i == 0:
            div.append((i, yellow//i))
        i += 1
    
    for i in range(len(div)):
        if div[i][0]*2 + div[i][1]*2 + 4 == brown:
            answer.append(div[i][1] + 2)
            answer.append(div[i][0] + 2)
            return answer
    
    answer.append(yellow + 2)
    answer.append(3)            # 1 + 2

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(50, 22))