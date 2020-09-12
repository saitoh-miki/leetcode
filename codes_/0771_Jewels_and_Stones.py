# %% [771. *Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)
# 問題：Jに含まれるSの文字数を返せ
# 解法：in演算子を用いる
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(c in J for c in S)
