# %% [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p = head
        q = p.next if p else p
        while q and q != p:
            p = p.next
            q = q.next
            q = q.next if q else q
        return q
