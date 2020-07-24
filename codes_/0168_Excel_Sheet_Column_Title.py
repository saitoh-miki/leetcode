# %% [168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)
class Solution:
    def convertToTitle(self, n: int) -> str:
        n, s = n - 1, ""
        while n > 25:
            n, s = n // 26 - 1, chr(n % 26 + 65) + s
        return chr(n + 65) + s
