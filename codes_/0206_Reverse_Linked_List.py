# %% [206. *Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans, p = None, head
        while p:
            ans = ListNode(p.val, ans)
            p = p.next
        return ans
