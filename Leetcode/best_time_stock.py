# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# 1. mine (time limit)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        
        for i in range(len(prices)-1):
            max_price = max(max_price, max(prices[i+1:])-prices[i])
        
        return max_price
"""

# 2. another way (1200 ms)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(price, min_price)
            profit = max(price-min_price, profit)
        
        return profit
