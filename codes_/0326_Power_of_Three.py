# %% [326. Power of Three](https://leetcode.com/problems/power-of-three/)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and round(math.log(n, 3), 14) % 1 == 0
