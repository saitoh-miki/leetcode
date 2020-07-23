# %% [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = q = head
        for _ in range(n + 1):
            if not q:
                return head.next
            q = q.next
        while q:
            p = p.next
            q = q.next
        p.next = p.next.next
        return head
