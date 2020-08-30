# %% [1389. *Create Target Array in the Given Order](https://leetcode.com/problems/create-target-array-in-the-given-order/)
# 問題：numsをindexの順に並べ替えよ
# 解法：list.insertを用いる
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for n, i in zip(nums, index):
            res.insert(i, n)
        return res
