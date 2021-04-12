import math

def solution(distance, rocks, n):
    left = 1            # 돌과 돌 사이의 최소 거리 (돌이 겹쳐 있지 않다는 가정)
    right = distance    # 돌과 돌 사이의 최대 거리
    answer = 0

    rocks.sort()        # 거리 순으로 정렬 

    while left <= right:
        mid = (left + right) // 2   # left, right 중앙값 (이분 탐색 기준)
        pre_rock = 0                # 이전 돌의 위치
        removed_rocks = 0           # 제거된 돌의 갯수
        min_dt = math.inf           # 실제 돌과 돌 사이의 거리 중 최소값 (math.inf : 무한대의 큰 값)

        for cur_rock in rocks:
            if cur_rock - pre_rock < mid:                   # 두 돌 사이의 거리가 기준 범위 이내면
                removed_rocks += 1                          # 돌을 제거
            else:                                           # 기준 범위 이외면 제거 하지 않고
                min_dt = min(min_dt, cur_rock - pre_rock)   # 실제 돌 사이의 거리 중 최소값을 구하고
                pre_rock = cur_rock                         # 현재 돌을 이전 돌의 위치값으로 변경
        
        if removed_rocks > n:                           # 제거된 돌의 갯수가 n개를 넘으면
            right = mid - 1                             # 바위 갯수를 줄여야 하기 때문에 기준을 낮춰야 함
        else:                                           # 제거된 돌의 갯수가 n개 이하면 
            #if removed_rocks == n: answer = min_dt     # 왜 이 조건으로 실행하면 오류가 날까?
            answer = min_dt
            left = mid + 1                              # 기준을 높여야 함
    
    return answer

"""
if removed_rocks == n: answer = min_dt
위 조건을 넣었을 때, 일부 테스트 케이스에서 원하는 값이 나오지 않았던 이유는
제거된 돌의 갯수가 n보다 작은 상황에서 (removed_rocks < n)
최소 거리(min_dt)가 정해지고 나면 최소 거리에 해당하는 두 돌 외의 어떤 돌을 삭제해도 답이 되기 때문이다.
    > 문제에서 구하는 답은 n개의 돌을 삭제했을 때 돌 사이의 최소값들 중 최댓값을 구하는 것이다. (모든 경우의 수에 대해)
따라서 removed_rocks <= n인 모든 경우에 대해 answer = min_dt를 해줘야 한다.
"""