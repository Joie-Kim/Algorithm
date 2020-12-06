import heapq

def solution(scoville, K):
    
    answer = 0
    
    heapq.heapify(scoville)
    
    for _ in range(len(scoville)):
        if scoville[0] >= K: break
        if len(scoville) == 1: return -1
        
        scov = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, scov)
        answer += 1
        
    return answer