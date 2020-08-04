# %% [506. Relative Ranks](https://leetcode.com/problems/relative-ranks/)


import numpy as np


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        d = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        e = dict(zip(sorted(nums, reverse=True), range(1, len(nums) + 1)))
        return [d.get(e[i], str(e[i])) for i in nums]
