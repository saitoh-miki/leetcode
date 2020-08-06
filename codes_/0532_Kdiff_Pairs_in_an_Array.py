# %% [532. K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = collections.Counter(nums)
        return sum(k > 0 and n + k in c or k == 0 and f > 1 for n, f in c.items())
