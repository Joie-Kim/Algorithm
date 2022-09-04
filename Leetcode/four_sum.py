class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            
            left1, right = i+1, len(nums)-1
            while left1 < right:
                left2, right = left1+1, len(nums)-1
                while left2 < right:
                    sum = nums[i] + nums[left1] + nums[left2] + nums[right]
                    if sum < target:
                        left2 += 1
                    elif sum > target:
                        right -= 1
                    else:
                        results.append((nums[i], nums[left1], nums[left2], nums[right]))
                        while left2 < right and nums[left2] == nums[left2+1]:
                            left2 += 1
                        while left2 < right and nums[right] == nums[right-1]:
                            right -= 1
                        left2 += 1
                        right -= 1
                left1 += 1
                while nums[left1] == nums[left1-1] and left1 < right:
                    left1 += 1
                    
        return results