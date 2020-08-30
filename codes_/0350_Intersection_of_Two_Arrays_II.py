# %% [350. *Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
# 問題：2つのリストの共通部分をリストで返せ
# 解法：collections.Counterを用いる
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = collections.Counter(nums1) & collections.Counter(nums2)
        return list(c.elements())
