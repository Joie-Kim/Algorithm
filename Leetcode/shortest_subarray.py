# 581. Shortest Unsorted Continuous Subarray

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        
        left, right = 0, len(nums)-1
        
        if left >= right: return 0 # length <= 1
        
        while left <= right:
            if sorted_nums[left] == nums[left] : left += 1
            else: break
        
        while left <= right:
            if sorted_nums[right] == nums[right] : right -= 1
            else: break
        
        return right - left + 1