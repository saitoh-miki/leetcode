# %% [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res, n, m = 0, len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res += 4
                if j + 1 < m and grid[i][j] == grid[i][j + 1] == 1:
                    res -= 2
                if i + 1 < n and grid[i][j] == grid[i + 1][j] == 1:
                    res -= 2
        return res
