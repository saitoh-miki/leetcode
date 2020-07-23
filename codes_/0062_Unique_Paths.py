# %% [62. Unique Paths](https://leetcode.com/problems/unique-paths/)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return round(math.factorial(m + n - 2) / math.factorial(n - 1) /
                     math.factorial(m - 1))
