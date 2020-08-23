# %% [485. *Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(itertools.accumulate(nums, lambda a, b: a * b + b))
