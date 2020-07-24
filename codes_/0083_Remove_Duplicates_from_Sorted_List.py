# %% [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p:
            while p.next and p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head
