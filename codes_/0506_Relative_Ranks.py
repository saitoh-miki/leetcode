# %% [506. Relative Ranks](https://leetcode.com/problems/relative-ranks/)


import numpy as np


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        d = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        n = (-np.array(nums)).argsort().argsort()
        return [d.get(i, str(i + 1)) for i in n]
