# %% [504. Base 7](https://leetcode.com/problems/base-7/)


class Solution:
    def convertToBase7(self, num: int) -> str:
        sign, num = "-" * (num < 0), abs(num)
        res = []
        while num:
            res.append(str(num % 7))
            num //= 7
        return sign + "".join(res[::-1] or ["0"])
