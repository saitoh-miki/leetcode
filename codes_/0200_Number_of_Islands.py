# %% [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        u = unionfind(n, m)
        for i in range(n):
            for j in range(m - 1):
                if grid\[i\][j] == grid\[i\][j + 1] == '1':
                    u.unite((i, j),  (i, j + 1))
        for i in range(n - 1):
            for j in range(m):
                if grid\[i\][j] == grid\[i + 1\][j] == '1':
                    u.unite((i, j),  (i + 1, j))
        return len(set(u.find(i, j) for i in range(n)
                   for j in range(m) if grid\[i\][j] == '1'))

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
