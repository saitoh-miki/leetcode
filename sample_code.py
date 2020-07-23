# %%
from leetcode import *  # noqa
from leetcode import List

# %% [1. Two Sum](https://leetcode.com/problems/two-sum/)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, ni in enumerate(nums):
            for j, nj in enumerate(nums[i + 1 :], i + 1):
                if ni + nj == target:
                    return [i, j]


# %%
Solution().twoSum([2, 7, 11, 15], 9)
