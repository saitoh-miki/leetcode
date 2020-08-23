# %% [172. *Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n < 5 else n // 5 + self.trailingZeroes(n // 5)
