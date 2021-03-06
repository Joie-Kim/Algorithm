# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# 44 ms
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def dfs(index, path):
            answer.append(path)
            
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        
        return answer