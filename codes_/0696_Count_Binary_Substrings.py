# %% [696. *Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings/)
# 問題：正規表現'(0+1+|1+0+)'にマッチする個数を返せ。ただし0と1は同数とする
# 解法：itertools.groupbyを用いる
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        lst = [len(list(g)) for _, g in itertools.groupby(s)]
        return sum(min(i, j) for i, j in zip(lst, lst[1:]))
