# %% [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        p1, p2, sm, mn = 0, -1, 0, -1
        while sm >= s or p2 < len(nums) - 1:
            if sm < s:
                sm += nums[(p2 := p2 + 1)]
            else:
                if mn < 0 or p2 - p1 < mn:
                    mn = p2 - p1
                sm -= nums[(p1 := p1 + 1) - 1]
        return mn + 1
