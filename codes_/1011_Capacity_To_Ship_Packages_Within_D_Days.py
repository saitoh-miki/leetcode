# %% [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            d, sm, md = 1, 0, (hi + lo) // 2
            for weight in weights:
                sm += weight
                if sm > md:
                    d, sm = d + 1, weight
            if d > D:
                lo = md + 1
            else:
                hi = md
        return hi
