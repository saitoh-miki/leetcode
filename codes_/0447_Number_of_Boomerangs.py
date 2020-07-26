# %% [447. Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/)
import numpy as np


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n, pts = 0, np.array(points)
        for pt in pts:
            c = collections.Counter([np.linalg.norm(i) for i in pts - pt])
            n += sum(i * (i - 1) for i in c.values())
        return n
