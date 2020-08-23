# %% [1. *Two Sum](https://leetcode.com/problems/two-sum/)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc = {}
        for i, num in enumerate(nums):
            if num in dc:
                return [dc[num], i]
            dc[target - num] = i
