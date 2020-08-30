# %% [485. *Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)
# 問題：同じ値が連続する部分リストの最大長を求めよ
# 解法：itertools.accumulateを用いる
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(itertools.accumulate(nums, lambda a, b: a * b + b))
