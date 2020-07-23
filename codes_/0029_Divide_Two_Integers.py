# %% [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

import numpy as np

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = dividend / divisor
        n = int(np.sign(n) * math.floor(abs(n)))
        return min(n, 2**31-1)
