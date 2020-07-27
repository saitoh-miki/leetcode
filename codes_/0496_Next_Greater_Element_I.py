# %% [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dc, cur = {}, []
        for i in nums2:
            while cur and i > cur[-1]:
                dc[cur.pop()] = i
            cur.append(i)
        return [dc.get(i, -1) for i in nums1]
