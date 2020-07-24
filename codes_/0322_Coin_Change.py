# %% [322. Coin Change](https://leetcode.com/problems/coin-change/)
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] + [math.inf] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i >= c else math.inf for c in coins]) + 1
        return -1 if math.isinf(dp[amount]) else dp[amount]
