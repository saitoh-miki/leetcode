# %% [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def calc(nums):
            robed, norob = 0, 0
            for num in nums:
                robed, norob = norob + num, max(robed, norob)
            return max(robed, norob)

        return max(sum(nums[:1]), calc(nums[:-1]), calc(nums[1:]))
