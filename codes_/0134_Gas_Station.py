# %% [134. Gas Station](https://leetcode.com/problems/gas-station/)

import numpy as np

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cs = (np.array(gas) - cost).cumsum()
        return -1 if cs[-1] < 0 else (cs.argmin() + 1) % len(gas)
