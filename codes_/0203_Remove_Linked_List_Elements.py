# %% [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = p = ListNode(0, head)
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return res.next
