# %% [53. *Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
# 問題：「連続部分列の和」の最大を求めよ
# 解法：要素nでは「そこまでの部分列の和+n」かnの大きい方が候補
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c, mx = 0, nums[0]
        for n in nums:
            c = max(c, 0) + n
            mx = max(mx, c)
        return mx
