# %% [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        u = unionfind(n, m)
        for i in range(n):
            for j in range(m):
                if j + 1 < m and grid[i][j] == grid[i][j + 1] == 1:
                    u.unite((i, j), (i, j + 1))
                if i + 1 < n and grid[i][j] == grid[i + 1][j] == 1:
                    u.unite((i, j), (i + 1, j))
        u = collections.Counter(
            u.find(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1
        ).most_common(1)
        return u[0][1] if u else 0


class unionfind:
    def __init__(self, n, m):
        self.m = m
        self.parent = list(range(n * m))

    def find(self, i, j):
        k = i * self.m + j
        while self.parent[k] != k:
            k = self.parent[k]
        return k

    def unite(self, p, q):
        self.parent[self.find(*q)] = self.find(*p)
