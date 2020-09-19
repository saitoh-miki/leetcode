# %% [896. Monotonic Array](https://leetcode.com/problems/monotonic-array/)
# 問題：広義の単調かどうかを返せ
# 解法：np.diffを用いる
import numpy as np


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        a = np.diff(A)
        return all(a >= 0) or all(a <= 0)
