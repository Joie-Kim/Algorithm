def solution(numbers, target):
    n = len(numbers)
    answer = 0
    
    def dfs(L, total):
        if L == n:
            if total == target:
                nonlocal answer
                answer += 1
        else:
            dfs(L+1, total+numbers[L])
            dfs(L+1, total-numbers[L])
    
    dfs(0,0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([1, 1, 2, 1, 2, 3, 5], 9))
print(solution([1, 1, 1, 3, 2, 2, 5], 9))