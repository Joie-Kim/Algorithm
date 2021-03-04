# 200. Number of Islands
# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# 140 ms
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """중첩함수 dfs 정의"""
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != '1':
                return
            
            # 방문한 땅일 경우 표시
            grid[i][j] = '#'
            
            # 동서남북으로 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # 섬의 개수를 담을 변수  
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # 깊이 우선 탐색으로 땅을 탐색
                    dfs(i, j)
                    count += 1
        
        return count