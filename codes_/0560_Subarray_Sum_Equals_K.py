# %% [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = total = 0
        dc = collections.defaultdict(int, {0: 1})
        for i in nums:
            total += i
            res += dc.get(total - k, 0)
            dc[total] += 1
        return res
