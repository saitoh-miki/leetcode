# %% [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return round(math.sqrt(num), 14) % 1 == 0
