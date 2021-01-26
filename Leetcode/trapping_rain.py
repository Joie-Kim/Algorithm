# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# 1. Using two pointer (60 ms)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        
        return volume
"""

# 2. Using stack (100 ms)
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0: break
                
                distance = i - stack[-1] - 1
                water = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * water
            
            stack.append(i)
        
        return volume
