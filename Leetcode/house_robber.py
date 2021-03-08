# 198. House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Time limit exceeded
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            
            return max(_rob(i - 1), _rob(i - 2) + nums[i])
        return _rob(len(nums) - 1)
"""

# Using Tabulation
# 순서가 유지되는 딕셔너리 사용
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        total = collections.OrderedDict()
        total[0], total[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            total[i] = max(total[i - 1], total[i - 2] + nums[i])
        
        # 가장 마지막 아이템을 pop 하는 함수 (value를 알기 위해 [1]를 사용했음)
        return total.popitem()[1]
"""

# Another way (32 ms)
# 딕셔너리 사용 안 하고, 리스트 사용
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        total = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            total.append(max(total[i - 1], total[i - 2] + nums[i]))
        
        return total[-1]
