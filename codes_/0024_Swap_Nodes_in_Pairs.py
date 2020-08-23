# %% [24. *Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        top = p = ListNode(0, head)
        while (q := p.next) and (r := q.next):
            p.next, q.next, r.next = r, r.next, q
            p = r.next
        return top.next
