# 785. Is Graph Bipartite?

from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        self.nodes = [-1]*n
        def bfs(s):
            self.nodes[s] = 0
            q = deque([s])
            while q:
                cur = q.popleft()
                for t in graph[cur]:
                    if self.nodes[t] == -1:
                        self.nodes[t] = self.nodes[cur] + 1
                        q.append(t)
                    elif self.nodes[t] == self.nodes[cur]:
                        return False
            return True
        return all(bfs(v) for v in range(n) if self.nodes[v] == -1)