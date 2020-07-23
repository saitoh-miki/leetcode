# %% [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = j = bisect.bisect_left(nums, target)
        if i == n or nums[i] != target:
            return [-1, -1]
        while j < n and nums[j] == nums[i]:
            j += 1
        return [i, j - 1]
