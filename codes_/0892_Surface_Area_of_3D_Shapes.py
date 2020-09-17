# %% [892. Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/)
# 問題：表面積の和を返せ
# 解法：NumPyを用いる
import numpy as np


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res, n1, n2, n3 = 0, len(grid), len(grid[0]), np.max(grid)
        dd = [(1, 1, 2), (1, 1, 0), (1, 2, 1), (1, 0, 1), (2, 1, 1), (0, 1, 1)]
        a = np.zeros((n1 + 2, n2 + 2, n3 + 2), int)
        for i, j in itertools.product(range(n1), range(n2)):
            a[i + 1, j + 1, 1 : grid[i][j] + 1] = 1
        for i, j, k in itertools.product(range(n1), range(n2), range(n3)):
            if a[i + 1, j + 1, k + 1]:
                res += 6 - sum(a[i + x, j + y, k + z] for x, y, z in dd)
        return res
