# 787. Cheapest Flights Within K Stops
# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

# 88 ms
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # 그래프 생성
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # 큐: (가격, 정점, 남은 경유지 수)
        queue = [(0, src, K)]
        
        while queue:
            price, node, k = heapq.heappop(queue)
            
            # 도착지라면 탐색 종료
            if node == dst:
                return price
            
            # 정해진 경유지 수 이내에서만 탐색
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(queue, (alt, v, k-1))
        
        return -1