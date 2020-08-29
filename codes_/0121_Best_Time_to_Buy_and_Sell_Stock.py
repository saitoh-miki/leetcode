# %% [121. *Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
# 問題：一度だけ買って売るときの最大利益を求めよ
# 解法：各価格で、そこまでの最小を更新しつつ売ったときの値で更新
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn, mx = math.inf, 0
        for price in prices:
            mn = min(mn, price)
            mx = max(mx, price - mn)
        return mx
