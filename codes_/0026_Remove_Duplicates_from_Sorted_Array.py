# %% [26. *Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
# 問題：ソート済みのリストから重複要素を除去し、修正後の長さを返せ
# 解法：前の要素と異なるものだけで作り直す（see 27）
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = None
        nums[:] = [p := i for i in nums if i != p]
        return len(nums)
