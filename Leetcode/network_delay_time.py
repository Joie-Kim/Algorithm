# 743. Network Delay Time
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# 488 ms
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 생성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 큐: (소요시간, 정점)
        queue = [(0, k)]
        # 정점에 도착하기까지 걸린 최소 소요시간
        dist = collections.defaultdict(int)
        
        while queue:
            time, node = heapq.heappop(queue)
            if node not in dist:                    # dist에 정점이 존재하지 않으면 (방문 안 했으면)
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(queue, (alt, v)) # 힙을 사용해서 최소 시간이 가장 먼저 pop 될 수 있도록 함
        
        if len(dist) == n:
            return max(dist.values())
        
        return -1