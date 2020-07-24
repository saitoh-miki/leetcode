# %% [1496. Path Crossing](https://leetcode.com/problems/path-crossing/)
import numpy as np


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dc = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
        a = np.cumsum([dc[c] for c in path], 0)
        c = collections.Counter([(0, 0)] + [tuple(i) for i in a])
        return max(c.values()) > 1
