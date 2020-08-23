# %% [122. *Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, j - i) for i, j in zip(prices, prices[1:]))
