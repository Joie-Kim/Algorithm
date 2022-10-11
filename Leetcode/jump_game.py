# 55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = 0
        i = 0
        
        while (i <= max_distance):
            print(i)
            max_distance = max(max_distance, i + nums[i])
            if (max_distance >= len(nums) - 1):
                return True
            i += 1
        
        return False
