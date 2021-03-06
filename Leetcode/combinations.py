# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# You may return the answer in any order.

# 472 ms
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        
        def dfs(elements, start, k):
            if k == 0:
                answer.append(elements[:])
                return
            
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        
        dfs([], 1, k)
        
        return answer

# Using itertools (68 ms)
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))
"""