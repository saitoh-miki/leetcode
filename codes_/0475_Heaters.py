# %% [475. Heaters](https://leetcode.com/problems/heaters/)
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0
        for house in houses:
            i = bisect.bisect(heaters, house)
            m = min(abs(house - heater) for heater in heaters[max(0, i - 1) : i + 1])
            res = max(res, m)
        return res
