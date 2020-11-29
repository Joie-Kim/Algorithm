def solution(priorities, location):
    from collections import deque
    
    answer = 0
    
    deque_pr = deque([(value, idx) for idx, value in enumerate(priorities)])
    
    while len(deque_pr):
        pr = deque_pr.popleft()
        
        if deque_pr and pr[0] < max(deque_pr)[0]:
            deque_pr.append(pr)
        else:
            answer += 1
            if pr[1] == location: break
    
    return answer