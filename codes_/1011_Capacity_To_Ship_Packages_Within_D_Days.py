# %% [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, u = max(weights), sum(weights)
        while l < u:
            d, s, m = 1, 0, (u + l) // 2
            for weight in weights:
                s += weight
                if s > m:
                    d, s = d + 1, weight
            if d > D:
                l = m + 1
            else:
                u = m
        return u
