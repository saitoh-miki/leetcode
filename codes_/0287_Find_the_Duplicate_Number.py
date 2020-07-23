# %% [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, v in enumerate(nums, 1):
            if v in nums[i:]:
                return v
