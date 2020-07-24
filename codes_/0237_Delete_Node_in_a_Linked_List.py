# %% [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)
class Solution:
    def deleteNode(self, node: ListNode):
        """void Do not return anything, modify node in-place instead."""
        node.val = node.next.val
        node.next = node.next.next
