def solution(progresses, speeds):
    import math
    import copy
    from collections import deque
    
    answer = []
    
    work_days = deque()
    
    for progress, speed in zip(progresses, speeds):
        work_day = math.ceil((100 - progress)/speed)
        work_days.append(work_day)
    
    while work_days:
        day = work_days.popleft()
        cnt = 1
        
        for _ in range(len(copy.deepcopy(work_days))): # 반복문을 사용하는 동안 deque 값이 변형되면 런타임 에러 남
            cmp_day = work_days[0]
            
            if cmp_day > day: break
            
            cnt += 1
            work_days.remove(cmp_day)
        
        answer.append(cnt)
    
    return answer