# %% [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(merge_sort(nums1, nums2))

def first(lst, default):
    return lst[0] if lst else default

def merge_sort(left, right):
    left, right = collections.deque(left), collections.deque(right)
    while left or right:
        is_left = first(left, math.inf) < first(right, math.inf)
        yield left.popleft() if is_left else right.popleft()
