# %% [35. *Search Insert Position](https://leetcode.com/problems/search-insert-position/)
# 問題：ソート済みのnumsにソートを維持する挿入位置を求めよ
# 解法：bisectモジュールを利用せよ
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
