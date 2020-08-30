# %% [693. *Binary Number with Alternating](https://leetcode.com/problems/binary-number-with-alternating-bits/)
# 問題：2進数にしたときに隣の文字が必ず異なるか求めよ
# 解法：binを用いる
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        return "00" not in s and "11" not in s
