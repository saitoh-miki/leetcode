# %% [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)

class Solution:
    def numberOfSteps (self, num: int) -> int:
        res = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num //= 2
            res += 1
        return res
