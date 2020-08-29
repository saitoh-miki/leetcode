# %% [78. *Subsets](https://leetcode.com/problems/subsets/)
# 問題：部分集合を列挙せよ
# 解法：要素の有無を引数にしてitertools.productを使う
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [sum(i, []) for i in itertools.product(*([[], [i]] for i in nums))]
