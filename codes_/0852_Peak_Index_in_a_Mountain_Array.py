# %% [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)
# 問題：最大値のインデックスを返せ（最大値の左右は狭義で単調）
# 解法：二分探索を用いる
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, up = 0, len(arr) - 1
        while up - lo > 1:
            mid = (lo + up) // 2
            if arr[mid] > arr[mid + 1]:
                up = mid
            else:
                lo = mid
        return up
