from collections import defaultdict

def solution(n, results):
    wins = defaultdict(set)     # wins[i] : i가 이긴 선수들의 집합 (i보다 실력 안 좋음)
    loses = defaultdict(set)    # loses[i] : i가 진 선수들의 집합 (i보다 실력 좋음)
    
    for i in range(1, n+1):     # 각 집합에 값을 넣음
        for result in results:
            if result[0] == i:
                wins[i].add(result[1])
            elif result[1] == i:
                loses[i].add(result[0])
    
    for i in range(1, n+1):
        for loser in wins[i]:               # i에게 진 선수라면
            loses[loser].update(loses[i])   # i가 진(i를 이긴) 선수에게도 무조건 진다.
        for winer in loses[i]:              # i에게 이긴 선수라면
            wins[winer].update(wins[i])     # i가 이긴(i에게 진) 선수를 무조건 이긴다.

    answer = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n - 1:   # i에 관련된 값이 n-1이면 순위를 알 수 있다.
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))