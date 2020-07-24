# %% [258. Add Digits](https://leetcode.com/problems/add-digits/)
class Solution:
    def addDigits(self, num: int) -> int:
        while len(s := str(num)) > 1:
            num = sum(int(c) for c in s)
        return num
