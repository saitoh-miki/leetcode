# %% [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        st = set()
        while head:
            i = id(head)
            if i in st:
                return head
            st.add(i)
            head = head.next
        return None
