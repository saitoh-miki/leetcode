# %% [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)
import numpy as np


class Solution:
    def reverse(self, x: int) -> int:
        x = np.sign(x) * int("".join(reversed(str(abs(x)))))
        return x if -(2 ** 31) <= x <= 2 ** 31 - 1 else 0
