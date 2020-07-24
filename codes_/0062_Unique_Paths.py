# %% [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        fac = math.factorial
        return round(fac(m + n - 2) / fac(n - 1) / fac(m - 1))
