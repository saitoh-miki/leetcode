# %% [21. *Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = tn = ListNode()
        inf, ll = math.inf, [l1, l2]
        while ll[0] or ll[1]:
            i = int((ll[0].val if ll[0] else inf) > (ll[1].val if ll[1] else inf))
            tn.next = tn = ListNode(ll[i].val)
            ll[i] = ll[i].next
        return res.next
