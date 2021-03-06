# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# 76 ms
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                answer.append(path)
                return
            
            for i in range(index, len(candidates)):
                # path.append(candidates[i])
                # csum -= candidates[i]
                dfs(csum - candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        
        return answer