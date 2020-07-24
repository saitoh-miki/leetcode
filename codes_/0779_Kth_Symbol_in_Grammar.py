# %% [779. K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/)
class Solution:
    def kthGrammar(self, _: int, K: int) -> int:
        return bin(K - 1).count("1") % 2
