# %% [231. Power of Two](https://leetcode.com/problems/power-of-two/)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count("1") == 1
