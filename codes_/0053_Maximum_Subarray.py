# %% [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c, mx = 0, nums[0]
        for n in nums:
            c = max(c, 0) + n
            mx = max(mx, c)
        return mx
