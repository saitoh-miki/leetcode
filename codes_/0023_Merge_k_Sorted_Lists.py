# %% [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = p = ListNode()
        while True:
            mni, mnq, mn = -1, None, math.inf
            for i, q in enumerate(lists):
                if q and q.val < mn:
                    mni, mnq, mn = i, q, q.val
            if not mnq:
                break
            lists[mni] = mnq.next
            p.next = p = ListNode(mn)
        return res.next
