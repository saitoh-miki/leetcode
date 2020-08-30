# %% [643. *Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
# 問題：長さkの連続する部分リストの平均の最大を求めよ
# 解法：itertools.accumulateを用いる
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        a = [0] + list(itertools.accumulate(nums))
        return max(j - i for i, j in zip(a, a[k:])) / k
