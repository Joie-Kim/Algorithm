def solution(n, times):
    left = 1                # 모든 사람을 심사하는 데 걸리는 최소 시간
    right = max(times) * n  # 모든 사람을 심사하는 데 걸리는 최대 시간
    answer = 0

    while left <= right:
        mid = (left + right) // 2   # left, right의 중앙값
        people = 0
        for t in times:             # 심사관 마다 반복
            people += mid // t      # mid 시간 안에 심사할 수 있는 사람의 수
            if people >= n: break   # 모든 대기자들을 심사 완료
        
        if people >= n:             # 모든 대기자들을 심사 완료 했다면
            answer = mid
            right = mid - 1         # 최대 시간을 줄여서 다시 비교
        else:                       # 아직 심사할 대기자가 남아 있다면
            left = mid + 1          # 최소 시간을 늘려서 다시 비교
            
    return answer