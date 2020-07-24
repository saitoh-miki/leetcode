# %% [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = p = ListNode(None, head)
        while q := p.next:
            if q.next and (v := q.val) == q.next.val:
                while q and q.val == v:
                    q = q.next
                p.next = q
            else:
                p.next = p = q
        return ans.next
