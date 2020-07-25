# %% [405. Convert a Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/)
class Solution:
    def toHex(self, num: int) -> str:
        return hex(num & (2 ** 32 - 1))[2:]
