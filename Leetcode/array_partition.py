# 561. Array Partition I
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# 1. mine (380 ms)
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        sum = 0
        while nums:
            a = nums.pop()
            b = nums.pop()
            sum += min(a, b)
        
        return sum
"""

# 2. another way 1 (616 ms)
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        
        return sum
"""

# 3. another way 2 (300 ms)
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        
        return sum
"""

# 4. Pythonic way (460 ms)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
        # [::2] : 2칸씩 건너뜀, 짝수 번째를 계산하는 것과 동일함
