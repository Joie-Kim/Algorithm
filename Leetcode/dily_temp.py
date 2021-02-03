# 739. Daily Temperatures
# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# 468 ms
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = [0] * len(T)
        stack = []
        
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                output[last] = i - last
            stack.append(i)
        
        return output