# %% [507. Perfect Number](https://leetcode.com/problems/perfect-number/)


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 6:
            return False
        n = int(num ** 0.5) + 1
        return num == sum(i + num // i for i in range(2, n) if not num % i) + 1
