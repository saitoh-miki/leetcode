# %% [697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array/)
# 問題：個数最大のグループの要素をすべて含む連続する部分リストの最小長を求めよ
# 解法：個数最大のグループは1とは限らない
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = collections.Counter(nums).most_common()
        n, dg, rv = len(nums), c[0][1], list(reversed(nums))
        return n - max(nums.index(v) + rv.index(v) for v, s in c if s == dg)
