# %% [594. Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        dc = collections.defaultdict(int)
        for num in nums:
            dc[num] += 1
            res = max(res, dc.get(num - 1, -n) + dc[num], dc[num] + dc.get(num + 1, -n))
        return res
