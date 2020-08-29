# %% [122. *Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
# 問題：何度も買って売れるときの最大利益を求めよ
# 解法：前回より上がれば利益として総和
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, j - i) for i, j in zip(prices, prices[1:]))
