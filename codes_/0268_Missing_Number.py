# %% [268. Missing Number](https://leetcode.com/problems/missing-number/)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (n := len(nums)) * (n + 1) // 2 - sum(nums)
