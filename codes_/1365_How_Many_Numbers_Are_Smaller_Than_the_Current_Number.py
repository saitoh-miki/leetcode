# %% [1365. *How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
# 問題：各要素の「自分より小さい要素の数」の和を求めよ
# 解法：ソートしてlist.indexを用いる
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = sorted(nums)
        return [lst.index(i) for i in nums]
