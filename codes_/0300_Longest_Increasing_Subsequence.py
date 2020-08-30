# %% [300. **Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
# 問題：単調増加する部分リストの最大長を求めよ
# 解法：nums[i]を最後の要素とする最大長をdp[i]として計算する
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            mx = max([d if n < num else 0 for d, n in zip(dp, nums)], default=0)
            dp.append(mx + 1)
        return max(dp, default=0)
