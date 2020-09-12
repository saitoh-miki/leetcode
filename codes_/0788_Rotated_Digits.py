# %% [788. Rotated Digits](https://leetcode.com/problems/rotated-digits/)
class Solution:
    def rotatedDigits(self, N: int) -> int:
        res = 0
        c1, c2 = {2, 5, 6, 9}, {3, 4, 7}
        for i in range(1, N + 1):
            flg = False
            while i:
                if (d := i % 10) in c2:
                    break
                flg |= d in c1
                i //= 10
            else:
                res += flg
        return res
