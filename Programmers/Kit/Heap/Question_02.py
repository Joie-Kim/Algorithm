import heapq

def solution(jobs):
    heap = []               # 요청이 들어온 작업
    time, start = 0, -1     # time: 시간, start: 작업 시작 시간
    cnt = 0                 # 처리한 작업의 수
    answer = 0              # 걸린 시간

    print(jobs)

    while cnt < len(jobs):
        print(len(jobs))
        
        """요청이 들어온 작업이 있으면 heap에 넣음"""
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(heap, [job[1], job[0]])
        
        """요청 처리"""
        if len(heap) == 0:              # 요청 들어온 작업이 없으면
            time += 1
        else:                           # 요청이 들어온 작업이 있으면
            print(heap)
            cnt += 1
            root = heapq.heappop(heap)
            print(root)
            start = time
            time += root[0]
            answer += (time - root[1])
            print(start, time, answer)
    
    return answer//len(jobs)