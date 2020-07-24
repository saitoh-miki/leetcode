# %% [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
class Solution:
    def search(self, nums: List[int], t: int) -> int:
        lo, hi, n0 = 0, len(nums), nums and nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            flg = (nums[mid] < n0) == (t < n0)
            v = nums[mid] if flg else (-math.inf if t < n0 else math.inf)
            if v < t:
                lo = mid + 1
            elif v > t:
                hi = mid
            else:
                return mid
        return -1
