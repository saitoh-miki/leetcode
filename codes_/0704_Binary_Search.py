# %% [704. Binary Search](https://leetcode.com/problems/binary-search/)
# 問題：targetに一致するインデックスを返せ。見つからなければ-1
# 解法：bisect.bisect_leftを用いる
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)
        return i if i < len(nums) and nums[i] == target else -1
