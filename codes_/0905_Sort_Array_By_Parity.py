# %% [905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)
# 問題：偶数と奇数に分けよ
# 解法：2つの内包表記
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [a for a in A if not a % 2] + [a for a in A if a % 2]
