# %% [1498. Number of Subsequences That Satisfy the Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res, mod = 0, 10**9 + 7
        nums.sort()
        for i, mn in enumerate(nums):
            if 2 * mn > target:
                break
            k = bisect.bisect(nums, target - mn, i)
            res += pow(2, k - 1 - i, mod)
        return res % mod
