# %% [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)
class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mi = (lo + hi) // 2
            if (whc := guess(mi)) == -1:
                hi = mi - 1
            elif whc == 1:
                lo = mi + 1
            else:
                lo = hi = mi
        return lo
