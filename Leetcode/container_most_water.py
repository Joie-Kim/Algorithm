# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        result = 0
        
        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            result = max(result, cur_area)
            
            if height[left] < height[right]: left += 1
            else: right -= 1
        
        return result