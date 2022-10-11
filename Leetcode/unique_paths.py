# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [[0] * (m) for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 : map[i][j] = 1
                else:
                    map[i][j] = map[i-1][j] + map[i][j-1]
        
        return map[-1][-1]