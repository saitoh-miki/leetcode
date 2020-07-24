# %% [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)
class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 0
        for c in s:
            n = n * 26 + ord(c) - 64
        return n
