# %% [883. Projection Area of 3D Shapes](https://leetcode.com/problems/projection-area-of-3d-shapes/)
# 問題：3方向から見たときの影の面積の和を返せ
# 解法：NumPyを用いる
import numpy as np


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        a = np.array(grid)
        return (a > 0).sum() + a.max(0).sum() + a.max(1).sum()
