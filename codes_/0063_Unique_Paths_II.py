# %% [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def calc(i, j):
            if grid\[i\][j] or (i == n - 1 and j == m - 1):
                return 1 - grid\[i\][j]
            return ((calc(i + 1, j) if i + 1 < n else 0) +
                    (calc(i, j + 1) if j + 1 < m else 0))
        n, m = len(grid), len(grid[0])
        return calc(0, 0)
