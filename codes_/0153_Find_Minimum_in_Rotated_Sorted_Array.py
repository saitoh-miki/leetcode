# %% [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi and nums[lo] > nums[hi]:
            mid = (lo + hi) // 2
            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
