# %% [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
class Solution:
    def getSum(self, a: int, b: int, msk=2 ** 32 - 1) -> int:
        while b:
            a, b = (a ^ b) & msk, ((a & b) << 1) & msk
        return a if a <= (msk // 2) else ~(a ^ msk)
