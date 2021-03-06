# %% [263. Ugly Number](https://leetcode.com/problems/ugly-number/)
class Solution:
    def isUgly(self, num: int) -> bool:
        if num > 0:
            for n in [2, 3, 5]:
                while num % n == 0:
                    num //= n
        return num == 1
