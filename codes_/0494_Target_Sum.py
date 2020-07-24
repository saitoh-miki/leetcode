# %% [494. Target Sum](https://leetcode.com/problems/target-sum/)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nz = nums.count(0)
        nums = tuple(i for i in nums if i)
        sm = sum(nums) - S
        if sm % 2:
            return 0

        @functools.lru_cache(None)
        def css(nums, ssm):
            if ssm <= 0 or not nums:
                return int(not ssm)
            return css(nums[:-1], ssm - nums[-1]) + css(nums[:-1], ssm)
        return css(nums, sm // 2) * 2 ** nz

