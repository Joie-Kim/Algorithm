# 122. Best Time to Buy and Sell Stock II
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# 64 ms
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                answer += prices[i+1] - prices[i]
        
        return answer

# Pythonic way (64 ms)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))
"""
