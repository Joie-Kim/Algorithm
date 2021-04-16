def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    
    answer = 0
    
    while True:
        pr = queue.pop(0)
        
        if any(pr[1] < q[1] for q in queue): # max() 사용 안 하고, any() 사용
            queue.append(pr)
        else:
            answer += 1
            if pr[0] == location: break
    
    return answer