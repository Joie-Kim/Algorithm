# 238. Product of Array Except Self
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# 1. mine (time limit)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            pd = 1
            for ln in nums[:i]:
                pd *= ln
            for rn in nums[i+1:]:
                pd *= rn
            output.append(pd)
            
        return output
"""

# 2. another way (320 ms)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        pd = 1
        for i in range(len(nums)):
            output.append(pd)
            pd *= nums[i]
        
        pd = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= pd
            pd *= nums[i]
            
        return output