# %% [868. Binary Gap](https://leetcode.com/problems/binary-gap/)
# 問題：2進数表記の1のインデックスを並べた時、隣り合うインデックスの差の最大値を返せ
# 解法：binを用いる
class Solution:
    def binaryGap(self, N: int) -> int:
        a = [i for i, c in enumerate(bin(N)) if c == "1"]
        if len(a) < 2:
            return 0
        return max(j - i for i, j in zip(a, a[1:]))
