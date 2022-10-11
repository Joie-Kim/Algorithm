# 45. Jump Game II

class Solution:
    def jump(self, nums: List[int]) -> int:
        pointer = 0
        max_reach = nums[pointer]
        temp_reach = 0
        jump = 0
        
        if len(nums) == 1: return 0
        
        while True:
            if max_reach >= len(nums) - 1: return jump + 1
            
            temp_reach = max_reach
            
            while pointer < max_reach:
                pointer += 1
                if pointer + nums[pointer] > temp_reach:
                    temp_reach = pointer + nums[pointer]
            
            max_reach = temp_reach
            jump += 1
        