# %% [322. Coin Change](https://leetcode.com/problems/coin-change/)
class Solution(object):
    def coinChange(self, coins, amount):
        @functools.lru_cache(None)
        def calc(a):
            if not a:
                return 0
            return min([calc(a - c) for c in coins if a >= c], default=math.inf) + 1

        return -1 if math.isinf(n := calc(amount)) else n
