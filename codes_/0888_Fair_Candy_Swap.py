# %% [888. *Fair Candy Swap](https://leetcode.com/problems/fair-candy-swap/)
# 問題：Aの1つとBの1つを交換し和を同じにするとき、交換する値を返せ
# 解法：Aの各値を交換するとしたとき、対応する値がBに存在するか調べる
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        d, sb = (sum(B) - sum(A)) // 2, set(B)
        for a in A:
            if (b := a + d) in sb:
                return a, b
