# %% [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i, num in enumerate(nums):
            mx = max([d if num > n else 0 for d, n in zip(dp, nums)], default=0)
            dp.append(mx + 1)
        return max(dp, default=0)
