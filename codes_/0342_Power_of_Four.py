# %% [342. Power of Four](https://leetcode.com/problems/power-of-four/)
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return re.match("0b1(?:00)*$", bin(num))
