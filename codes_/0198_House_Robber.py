# %% [198. House Robber](https://leetcode.com/problems/house-robber/)
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for i in nums:
            pre, cur = cur, max(pre + i, cur)
        return cur
