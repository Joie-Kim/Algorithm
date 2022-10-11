# 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_arr = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_arr.append((i, j))
        
        for (x, y) in zero_arr:
            for j in range(n):
                matrix[x][j] = 0
            for i in range(m):
                matrix[i][y] = 0