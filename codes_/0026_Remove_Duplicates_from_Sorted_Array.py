# %% [26. *Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = None
        nums[:] = [p := i for i in nums if i != p]
        return len(nums)
