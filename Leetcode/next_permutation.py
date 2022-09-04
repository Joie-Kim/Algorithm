# 31. Next Permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) <= 1: return
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                for j in range(len(nums)-1, i, -1):
                    if nums[i] < nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        break
                break
            else:
                if i == 0: nums.sort()
        