# %% [171. *Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)
# 問題：Excelの列から順番を求めよ
# 解法：26進法として計算せよ
class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 0
        for c in s:
            n = n * 26 + ord(c) - 64
        return n
